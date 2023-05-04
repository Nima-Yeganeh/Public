sudo apt-get update -y
sudo apt-get install openssl -y
sudo apt-get upgrade openssl -y
ldconfig -p | grep libssl
sudo ldconfig -v
