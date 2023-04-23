docker exec -it docker-test5-wordpress-1 bash -c "wp rewrite structure '/%%postname%%/' --allow-root"
docker exec -it docker-test5-wordpress-1 bash -c "wp rewrite flush --allow-root"
