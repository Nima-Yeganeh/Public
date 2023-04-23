docker-compose down
docker volume rm docker-test5_db_data
docker volume rm docker-test5_redis_data
docker volume rm docker-test5_wp_content
docker-compose down
docker-compose up -d
docker ps -a
