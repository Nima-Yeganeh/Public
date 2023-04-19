provider "docker" {
  host = "tcp://localhost:2375/"
}

resource "docker_image" "example" {
  name = "nginx:latest"
}

resource "docker_container" "example" {
  name  = "example-nginx"
  image = docker_image.example.latest
  ports {
    internal = 80
    external = 8080
  }
  restart = "always"
}
