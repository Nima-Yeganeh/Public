cat /etc/ansible/hosts

ansible --list-hosts all
ansible --list-hosts routers

ansible 192.168.244.101 -m raw -a 'show version' -u cisco -k
