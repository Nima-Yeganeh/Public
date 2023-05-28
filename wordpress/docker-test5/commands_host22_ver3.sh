targethost="docker-test5-wordpress22-1"
zurl="http://fi.domain.local"
title="Just Another Blog"
dbname="wordpress"
dbuser="wordpress"
dbpass="your_wordpress_password"
dbhost="db"
dbprefix="wp_"
admin_user="admin"
admin_password="P@ssw0rd"
admin_email="admin@domain.local"
docker exec -it $targethost bash -c "wp --info"
docker exec -it $targethost bash -c "wp core config --dbname=$dbname --dbuser=$dbuser --dbpass=$dbpass --dbhost=$dbhost --dbprefix=$dbprefix --path=/var/www/html --allow-root"
docker exec -it $targethost bash -c "wp core install --url=$zurl --title='$title' --admin_user=$admin_user --admin_password=$admin_password --admin_email=$admin_email --path=/var/www/html --allow-root --skip-email"
docker exec -it $targethost bash -c "wp config list --allow-root"
docker exec -it $targethost bash -c "wp config set WP_POST_REVISIONS 0 --allow-root"
docker exec -it $targethost bash -c "wp core update --allow-root"
docker exec -it $targethost bash -c "wp core update-db --allow-root"
docker exec -it $targethost bash -c "wp config set WP_CACHE_KEY_SALT your-unique-salt-here --allow-root"
docker exec -it $targethost bash -c "wp config set WP_REDIS_PORT 6379 --allow-root"
docker exec -it $targethost bash -c "wp config set WP_REDIS_PASSWORD your-redis-password-here --allow-root"
docker exec -it $targethost bash -c "wp config set WP_REDIS_MAXTTL 86400 --allow-root"
docker exec -it $targethost bash -c "wp plugin install redis-cache --activate --allow-root"
docker exec -it $targethost bash -c "wp redis enable --force --allow-root"
docker exec -it $targethost bash -c "wp redis status --allow-root"
docker exec -it $targethost bash -c "wp plugin delete akismet --allow-root"
docker exec -it $targethost bash -c "wp plugin delete hello --allow-root"
docker exec -it $targethost bash -c "wp plugin install disable-comments --activate --allow-root"
docker exec -it $targethost bash -c "wp disable-comments delete --types=all --allow-root"
docker exec -it $targethost bash -c "wp disable-comments settings --types=all --allow-root"
docker exec -it $targethost bash -c "wp plugin install wordpress-seo --activate --allow-root"
docker exec -it $targethost bash -c "wp disable-comments settings --types=all --allow-root"
docker exec -it $targethost bash -c "wp yoast index --allow-root"
docker exec -it $targethost bash -c "wp post delete $(wp post list --post_type='page' --format=ids --allow-root) --allow-root"
docker exec -it $targethost bash -c "wp post list --post_type=page --allow-root"
docker exec -it $targethost bash -c "wp post delete $(wp post list --post_type='post' --format=ids --allow-root) --allow-root"
docker exec -it $targethost bash -c "wp post list --post_type=post --allow-root"
docker exec -it $targethost bash -c "wp theme activate twentytwentytwo --allow-root"
docker exec -it $targethost bash -c "wp --info"
docker exec -it $targethost bash -c "wp rewrite structure '/%year%/%monthnum%/%postname%/' --allow-root"
docker exec -it $targethost bash -c "wp rewrite structure '/%postname%/' --allow-root"
docker exec -it $targethost bash -c "wp cache flush --allow-root"
docker exec -it $targethost bash -c "wp rewrite flush --allow-root"
