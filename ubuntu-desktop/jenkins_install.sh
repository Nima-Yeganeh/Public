sudo apt update -y

curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update -y
sudo apt-get install fontconfig openjdk-11-jre -y
sudo apt install openjdk-17-jdk wget -y
sudo apt install default-jdk -y
sudo apt-get install jenkins -y
sudo apt update -y
sudo systemctl start jenkins
sudo systemctl enable jenkins
echo 'http://your_server_ip_or_domain:8080'
sudo systemctl status jenkins
ufw allow 8088
# sudo ufw enable
cat /var/lib/jenkins/secrets/initialAdminPassword
