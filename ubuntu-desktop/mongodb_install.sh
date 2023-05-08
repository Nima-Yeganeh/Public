sudo apt update -y
sudo apt install wget curl gnupg2 software-properties-common apt-transport-https ca-certificates lsb-release -y
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/mongodb-6.gpg
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt update -y
sudo apt install mongodb-org -y
sudo systemctl enable --now mongod
sudo systemctl status mongod
mongod --version
sudo cat /etc/mongod.conf
sudo systemctl restart mongod
sudo systemctl stop mongod
sudo systemctl daemon-reload
sudo systemctl start mongod
