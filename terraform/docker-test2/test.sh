docker-compose up -d
docker-compose exec terraform terraform init
docker-compose exec terraform terraform apply
