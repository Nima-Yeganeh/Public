sudo gitlab-rake gitlab:env:info
sudo ufw allow https
sudo ufw allow http
sudo ufw allow ssh
sudo ufw reload
cat /etc/gitlab/gitlab.rb
sudo gitlab-ctl reconfigure
sudo gitlab-ctl start
sudo gitlab-ctl status
sudo gitlab-ctl start
# sudo rm /etc/apt/sources.list.d/gitlab_gitlab-ce.list
