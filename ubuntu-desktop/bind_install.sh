sudo apt update -y
sudo apt install bind9 -y
cat /etc/bind/named.conf.options

sudo systemctl restart bind9
