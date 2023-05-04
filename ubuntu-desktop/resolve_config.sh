sudo echo '' > /etc/resolv.conf
sudo echo 'nameserver 8.8.8.8' >> /etc/resolv.conf
sudo echo 'nameserver 1.1.1.1' >> /etc/resolv.conf
cat /etc/resolv.conf
