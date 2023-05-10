hostnamectl set-hostname jenkins
yum update -y
yum install java-1.8.0-openjdk-devel -y
yum install sudo -y
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
yum repolist
yum install fontconfig java-11-openjdk -y
java --version
yum install jenkins -y
systemctl start jenkins
systemctl enable jenkins
systemctl status jenkins
yum search jenkins --showduplicates
cat /var/lib/jenkins/secrets/initialAdminPassword
