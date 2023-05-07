sudo apt-get update
sudo apt-get install snapd
sudo snap install minikube
sudo snap install kubectl --classic
sudo snap install kube-apiserver --classic
sudo snap start kube-apiserver.daemon
