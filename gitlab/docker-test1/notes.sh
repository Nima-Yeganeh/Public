docker-compose exec web grep 'Password:' /etc/gitlab/initial_root_password
docker-compose exec -it web /bin/bash
docker-compose exec web gitlab-rails runner "user = User.where(id: 1).first; user.password = 'P@ssw0rd'; user.password_confirmation = 'P@ssw0rd'; user.save!"
# login with user >> root >> password >> P@ssw0rd
docker-compose exec web ssh-keygen -t ed25519 -C "admin@domain.local"
docker-compose exec web cat /root/.ssh/id_ed25519.pub
docker-compose exec runner gitlab-runner register
