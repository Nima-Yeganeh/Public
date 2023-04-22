apt-get update
apt-get install -y less curl
# apt-get install php-cli php-mbstring unzip

curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
chmod +x wp-cli.phar
mv wp-cli.phar /usr/local/bin/wp
wp --info

wp core download --locale=en_US --path=/var/www/html --allow-root
wp core config --dbname=wordpress --dbuser=wordpress --dbpass=your_wordpress_password --dbhost=db --dbprefix=wp_ --path=/var/www/html --allow-root
wp core install --url=http://domain.local --title='Just Another Blog' --admin_user=admin --admin_password=P@ssw0rd --admin_email=admin@domain.local --path=/var/www/html --allow-root --skip-email
wp rewrite structure '/%postname%/' --allow-root

docker-compose up -d
docker-compose logs wordpress -f
docker exec -it docker-test4-wordpress-1 bash
