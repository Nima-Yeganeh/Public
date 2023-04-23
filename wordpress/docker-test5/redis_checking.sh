
redis-cli info server
redis-cli info memory
redis-cli info keyspace
redis-cli config get *
redis-cli monitor
redis-cli keys *

docker exec -it docker-test5-redis-1 redis-cli ping
docker exec -it docker-test5-redis-1 redis-cli info server
docker exec -it docker-test5-redis-1 redis-cli keys *

docker exec -it docker-test5-redis-1 redis-cli
AUTH your-redis-password-here
ping
keys *
