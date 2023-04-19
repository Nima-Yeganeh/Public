provider "vsphere" {
  user           = "administrator@vsphere.local"
  password       = "your-password"
  vsphere_server = "your-vsphere-server.com"
}

data "vsphere_datacenter" "dc" {
  name = "your-datacenter-name"
}

data "vsphere_datastore" "ds" {
  name          = "your-datastore-name"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network_interface" "nic" {
  label          = "Network adapter 1"
  network_id     = "your-network-id"
  datacenter_id  = data.vsphere_datacenter.dc.id
}

resource "vsphere_virtual_machine" "example" {
  name             = "example-vm"
  num_cpus         = 2
  memory           = 4096
  guest_id         = "ubuntu64Guest"
  scsi_type        = "pvscsi"
  datastore_id     = data.vsphere_datastore.ds.id
  network_interface {
    network_id     = data.vsphere_network_interface.nic.network_id
    adapter_type   = "vmxnet3"
  }

  disk {
    label          = "example-disk"
    size           = 20
  }

  cdrom {
    datastore_id   = data.vsphere_datastore.ds.id
    path           = "/path/to/iso"
  }

  clone {
    template_uuid  = "your-template-uuid"
  }

  provisioner "file" {
    source         = "example-file"
    destination    = "/path/on/vm/example-file"
  }

  provisioner "remote-exec" {
    inline         = [
      "echo 'Hello, World!'",
    ]
  }
}
