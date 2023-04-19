provider "docker" {
  host = "tcp://alpine:2375/"
}

resource "docker_container" "alpine" {
  name  = "alpine"
  image = "alpine:latest"
  command = ["/bin/sleep", "1000"]
}
