sudo apt-get update -y
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
sudo apt install -y tzdata curl ca-certificates openssh-server
gpg_key_url="https://packages.gitlab.com/gitlab/gitlab-ce/gpgkey"
curl -fsSL $gpg_key_url| sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gitlab.gpg
sudo tee /etc/apt/sources.list.d/gitlab_gitlab-ce.list<<EOF
deb https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/ focal main
deb-src https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/ focal main
EOF
sudo apt update -y
sudo apt-get install gitlab-runner -y
