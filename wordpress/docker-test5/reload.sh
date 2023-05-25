docker compose down
docker volume rm docker-test5_db1_data
docker volume rm docker-test5_redis1_data
docker volume rm docker-test5_wordpress1_content
docker volume rm docker-test5_db2_data
docker volume rm docker-test5_redis2_data
docker volume rm docker-test5_wordpress2_content
docker volume rm docker-test5_db3_data
docker volume rm docker-test5_redis3_data
docker volume rm docker-test5_wordpress3_content
docker volume rm docker-test5_db4_data
docker volume rm docker-test5_redis4_data
docker volume rm docker-test5_wordpress4_content
docker compose up -d
docker ps -a

