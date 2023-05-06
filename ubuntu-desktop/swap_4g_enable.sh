sudo swapoff -v /swapfile
sudo dd if=/dev/zero of=/swapfile2 bs=1G count=4
sudo chmod 600 /swapfile2
sudo mkswap /swapfile2
sudo swapon /swapfile2
echo '/swapfile2 swap swap defaults 0 0' >> /etc/fstab
cat /etc/fstab
