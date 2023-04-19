provider "ibm" {
  region      = "us-south"
  generation  = 2
}

resource "ibm_container_cluster" "example" {
  name            = "example-cluster"
  datacenter      = "dal13"
  machine_type    = "u2c.2x4"
  worker_pools {
    name          = "example-pool"
    machine_type  = "u2c.2x4"
    worker_nodes  = 1
  }
}

resource "ibm_container_namespace" "example" {
  name       = "example-namespace"
  cluster_id = ibm_container_cluster.example.id
}

resource "ibm_container_registry" "example" {
  name       = "example-registry"
  region     = "us-south"
  namespace  = ibm_container_namespace.example.name
}

resource "ibm_container_registry_namespace" "example" {
  name                 = "example-registry-namespace"
  registry_id          = ibm_container_registry.example.id
  resource_group_id    = data.ibm_resource_group.example.id
  registry_region_name = "us-south"
}

module "ibm_kubernetes_cluster" {
  source = "terraform-ibm-modules/kubernetes-ibmcloud/kubernetes"

  cluster_name = ibm_container_cluster.example.name
  region       = provider.ibm.region
  resource_group_id = data.ibm_resource_group.example.id
  cluster_config = {
    worker_pools = ibm_container_cluster.example.worker_pools
  }
}
