In this configuration, we have two services: db and wordpress. The db service uses the MySQL 5.7 image and creates a volume for persisting data. The wordpress service uses the latest WordPress image and maps port 8000 on the host to port 80 on the container. It also sets environment variables to connect to the MySQL database created by the db service.

To use this configuration, create a new file named docker-compose.yml and copy and paste the above configuration into it. Then, run the following command in the same directory as the docker-compose.yml file:

docker-compose up -d

This will start the two services in the background. Once they're up and running, you should be able to access WordPress by going to http://localhost:8000 in your web browser.
