wget https://github.com/prometheus/prometheus/releases/download/v2.30.2/prometheus-2.30.2.linux-amd64.tar.gz
tar xvfz prometheus-2.30.2.linux-amd64.tar.gz
sudo mv prometheus-2.30.2.linux-amd64 /opt/prometheus
sudo useradd --no-create-home --shell /bin/false prometheus
sudo chown -R prometheus:prometheus /opt/prometheus
sudo cp -f prometheus.service /etc/systemd/system/prometheus.service
cat /etc/systemd/system/prometheus.service
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl status prometheus
echo 'http://localhost:9090'
echo 'done!'

