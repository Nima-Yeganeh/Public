sudo nano /etc/systemd/system/prometheus.service
sudo vi /etc/systemd/system/prometheus.service

# Add the following content to the file:
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/opt/prometheus/prometheus --config.file=/opt/prometheus/prometheus.yml --storage.tsdb.path=/opt/prometheus/data
Restart=always

[Install]
WantedBy=multi-user.target

# other commands
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl status prometheus

# http://localhost:9090
