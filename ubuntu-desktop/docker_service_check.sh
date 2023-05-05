sudo systemctl status docker
sudo systemctl start docker
sudo netstat -tuln | grep 2375
# sudo usermod -aG docker $(whoami)
docker --version
