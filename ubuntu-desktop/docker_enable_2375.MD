sudo vi /usr/lib/systemd/system/docker.service

# add the line below where you find ExecStart (under Service section):
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock

sudo systemctl daemon-reload
sudo systemctl restart docker.service
sudo netstat -tuln | grep 2375
sudo docker ps -a
