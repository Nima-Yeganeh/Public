sudo apt update -y
sudo apt upgrade -y
sudo systemctl start docker
sudo systemctl enable docker
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo apt install kubectl
minikube start
kubectl version
docker version
minikube version
