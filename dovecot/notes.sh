sudo apt-get update
sudo apt-get install dovecot-core dovecot-imapd dovecot-pop3d
sudo yum install dovecot

cat /etc/dovecot/dovecot.conf

sudo systemctl start dovecot
sudo systemctl start dovecot.service

sudo systemctl status dovecot
sudo systemctl status dovecot.service

