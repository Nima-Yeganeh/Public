sudo hostnamectl set-hostname kubernetes-master
sudo hostnamectl set-hostname kubernetes-worker
sudo kubeadm init
kubectl get pods --all-namespaces
kubectl get nodes
