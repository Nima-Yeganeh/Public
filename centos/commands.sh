useradd testuser
cat /etc/passwd | grep testuser
# passwd testuser
cat /etc/shadow | grep testuser
groupadd testgroup

useradd testuser1 -G testgroup
# passwd testuser1

useradd testuser2 -g 1002
# passwd testuser2

yum -y install quota
repquota -as

yum install httpd vsftpd

systemctl start httpd
service httpd start

service status httpd
systemctl status httpd

systemctl start vsftpd
service vsftpd start

service status ftpd
systemctl status ftpd

getenforce

sestatus


sudo yum install bridge-utils SDL net-tools
sudo yum install centos-release-xen
sudo yum install xen
sudo yum install kernel-xen

