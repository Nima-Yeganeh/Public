apt update -y
apt install net-tools -y
apt install apt-utils -y
apt install inetutils-ping -y
apt install git -y
apt install software-properties-common -y
apt-add-repository --yes --update ppa:ansible/ansible
apt install ansible -y
ansible --version
