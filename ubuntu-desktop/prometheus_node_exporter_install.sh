sudo apt-get update -y
sudo apt-get install prometheus-node-exporter -y
sudo systemctl enable prometheus-node-exporter
sudo systemctl status prometheus-node-exporter
