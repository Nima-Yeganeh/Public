# Use the official WordPress image as the base image
FROM wordpress:5.5.0-php7.4-apache

# Set the working directory
WORKDIR /var/www/html

RUN apt-get update
RUN apt-get install -y less curl
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN chmod +x wp-cli.phar
RUN mv wp-cli.phar /usr/local/bin/wp
RUN wp --info
RUN wp core download --locale=en_US --path=/var/www/html --allow-root

# Expose port 80
EXPOSE 80
