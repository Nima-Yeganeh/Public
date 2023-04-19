provider "alicloud" {
  access_key = "your-access-key"
  secret_key = "your-secret-key"
  region     = "your-region"
}

resource "alicloud_cs_kubernetes" "example" {
  name               = "example-cluster"
  region_id          = "your-region"
  vpc_id             = "your-vpc-id"
  worker_instance_type = "ecs.n4.small"
  worker_system_disk_category = "cloud_ssd"
  worker_system_disk_size = "40"
  worker_vswitch_ids = ["your-vswitch-id"]
  worker_numbers = 3
  kubernetes_version = "1.18.8-aliyun.1"
  container_cidr     = "172.16.0.0/16"
  service_cidr       = "172.20.0.0/16"
  master_instance_type = "ecs.n4.small"
  master_system_disk_category = "cloud_ssd"
  master_system_disk_size = "40"
  master_vswitch_id = "your-vswitch-id"
  snat_entry         = true
  tags = {
    Environment = "dev"
  }
}

output "kubeconfig" {
  value = alicloud_cs_kubernetes.example.kube_config_raw
}
