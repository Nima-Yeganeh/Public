provider "digitalocean" {
  token = "your-digitalocean-api-token"
}

resource "digitalocean_droplet" "example" {
  image  = "ubuntu-18-04-x64"
  name   = "example-droplet"
  region = "nyc1"
  size   = "s-1vcpu-1gb"
}
