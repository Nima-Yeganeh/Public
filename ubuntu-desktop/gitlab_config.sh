sudo gitlab-rake gitlab:env:info
sleep 5
sudo ufw allow https
sudo ufw allow http
sudo ufw allow ssh
sudo ufw reload
sleep 5
cat /etc/gitlab/gitlab.rb
sleep 5
sudo gitlab-ctl reconfigure
sleep 5
sudo gitlab-ctl start
sudo gitlab-ctl status
sudo gitlab-ctl start
# sudo rm /etc/apt/sources.list.d/gitlab_gitlab-ce.list
