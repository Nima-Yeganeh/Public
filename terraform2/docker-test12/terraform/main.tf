provider "docker" {
  host = "tcp://localhost:2375/"
}

resource "docker_image" "ubuntu" {
  name = "ubuntu"
}

resource "docker_container" "ubuntu_container" {
  name  = "ubuntu_container"
  image = docker_image.ubuntu.latest
  command = ["sleep", "3600"]
  ports {
    internal = 80
    external = 8080
  }
}
