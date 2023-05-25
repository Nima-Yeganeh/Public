docker exec -it docker-test5-wordpress3-1 bash -c "wp --info"
docker exec -it docker-test5-wordpress3-1 bash -c "wp rewrite structure '/%year%/%monthnum%/%postname%/' --allow-root"
docker exec -it docker-test5-wordpress3-1 bash -c "wp rewrite structure '/%postname%/' --allow-root"
docker exec -it docker-test5-wordpress3-1 bash -c "wp cache flush --allow-root"
docker exec -it docker-test5-wordpress3-1 bash -c "wp rewrite flush --allow-root"

