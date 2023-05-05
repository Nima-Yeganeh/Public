#!/bin/bash

# Update the package repository
sudo apt-get update

# Install the required software packages
sudo apt-get install -y apache2 mysql-server php php-mysql

# Start the Apache web server
sudo systemctl start apache2

# Start the MySQL server
sudo systemctl start mysql

# Enable the Apache and MySQL services to start automatically on boot
sudo systemctl enable apache2
sudo systemctl enable mysql

# Print a message indicating that the installation was successful
echo "Software installation complete."
