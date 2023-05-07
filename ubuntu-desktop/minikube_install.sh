sudo apt update -y
sudo apt upgrade -y
sudo systemctl start docker
sudo systemctl enable docker
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

sudo apt update -y
sudo apt install curl -y
sudo apt-get install gnupg2 apt-transport-https ca-certificates software-properties-common -y

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/kubernetes-archive-keyring.gpg add -
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt update -y
sudo apt install kubectl -y

minikube start
kubectl version
docker version
minikube version
