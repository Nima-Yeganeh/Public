docker exec -it docker-test5-wordpress-1 bash -c "wp --info"
docker exec -it docker-test5-wordpress-1 bash -c "wp core config --dbname=wordpress --dbuser=wordpress --dbpass=your_wordpress_password --dbhost=db --dbprefix=wp_ --path=/var/www/html --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp core install --url=http://domain.local --title='Just Another Blog' --admin_user=admin --admin_password=P@ssw0rd --admin_email=admin@domain.local --path=/var/www/html --allow-root --skip-email"
docker exec -it docker-test5-wordpress-1 bash -c "wp rewrite structure '/%postname%/' --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp rewrite flush --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp theme activate twentytwentytwo --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp config list --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp config set WP_REDIS_HOST redis --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp config set WP_CACHE_KEY_SALT your-unique-salt-here --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp config set WP_REDIS_PORT 6379 --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp config set WP_REDIS_PASSWORD your-redis-password-here --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp config set WP_REDIS_MAXTTL 86400 --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp plugin install redis-cache --activate --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp redis enable --force --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp redis status --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp plugin delete akismet --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp plugin delete hello --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp plugin install disable-comments --activate --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp disable-comments delete --types=all --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp disable-comments settings --types=all --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp plugin install wordpress-seo --activate --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp disable-comments settings --types=all --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp post delete $(wp post list --post_type='page' --format=ids --allow-root) --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp post list --post_type=page --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp post delete $(wp post list --post_type='post' --format=ids --allow-root) --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp post list --post_type=post --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp config set WP_POST_REVISIONS 0 --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp core update --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp core update-db --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp rewrite structure '/%postname%/' --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp rewrite flush --allow-root"
