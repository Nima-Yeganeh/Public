#!/bin/bash

# Prompt the user for the lower and higher numbers
echo "Enter the lower number: "
read lower
echo "Enter the higher number: "
read higher

echo "**** Started ****"
tempfile=""
newtempfile="set_host_config_rev2.sh"
# Loop through the numbers between the lower and higher numbers
for (( i=$lower; i<=$higher; i++ )); do
	echo $i
	template_number=$i
	echo "bash commands_host"$template_number"_ver3.sh" >> $newtempfile
	echo "$newtempfile file updated!"
done
cat $newtempfile
echo "**** Done ****"
