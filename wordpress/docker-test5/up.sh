echo '**** Started ****'
bash reload.sh
echo '**** Configuring ****'
sleep 10
bash set_host_config_rev2.sh
echo '**** Done ****'
