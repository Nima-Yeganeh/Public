docker-compose down
docker volume rm docker-test5_db1_data
docker volume rm docker-test5_redis1_data
docker volume rm docker-test5_wordpress1_content
docker volume rm docker-test5_db2_data
docker volume rm docker-test5_redis2_data
docker volume rm docker-test5_wordpress2_content
docker-compose down
docker-compose up -d
docker ps -a
