sudo vi /etc/prometheus/prometheus.yml
sudo vi /opt/prometheus/prometheus.yml

# Add the following configuration to the scrape_configs section of the file:
- job_name: 'ubuntu'
  static_configs:
  - targets: ['<ubuntu-host-ip>:9100']

Replace `<ubuntu-host-ip>` with the IP address of the Ubuntu host.

# Restart the service
sudo systemctl restart prometheus

# Verify that Prometheus is able to scrape metrics from the Ubuntu host. You can do this by navigating to the Prometheus web interface (usually located at http://localhost:9090) and executing a query for the Ubuntu host metrics. For example, you can execute the following query to get the CPU usage of the Ubuntu host:
node_cpu{job="ubuntu"}
This should return a graph of the CPU usage for the Ubuntu host.

