provider "openstack" {
  user_name   = "your-openstack-username"
  tenant_name = "your-openstack-tenant-name"
  password    = "your-openstack-password"
  auth_url    = "http://your-openstack-auth-url:5000/v3/"
}

resource "openstack_compute_instance_v2" "example" {
  name            = "example-instance"
  flavor_name     = "m1.small"
  image_name      = "Ubuntu 18.04"
  key_pair        = "example-key"
  security_groups = ["default"]

  network {
    name = "example-network"
  }
}
