#!/bin/bash

# Prompt the user for the lower and higher numbers
echo "Enter the lower number: "
read lower
echo "Enter the higher number: "
read higher

echo "**** Started ****"
tempfile="docker_compose_template"
# Loop through the numbers between the lower and higher numbers
for (( i=$lower; i<=$higher; i++ )); do
	echo $i
	template_number=$i
	newtempfile=$tempfile$template_number
	# cat $tempfile
	cat $tempfile | sed "s/db1/db$template_number/g" | sed "s/redis1/redis$template_number/g" | sed "s/wordpress1/wordpress$template_number/g" > $newtempfile
	# echo 'done!'
	echo "$newtempfile file created!"
done

echo "**** Done ****"

