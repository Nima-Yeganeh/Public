#!/bin/bash

# Prompt the user for the lower and higher numbers
echo "Enter the lower number: "
read lower
echo "Enter the higher number: "
read higher

echo "**** Started ****"
tempfile="down_temp"
newtempfile="down.sh"
# Loop through the numbers between the lower and higher numbers
for (( i=$lower; i<=$higher; i++ )); do
	echo $i
	template_number=$i
	cat $tempfile | sed "s/db1/db$template_number/g" | sed "s/redis1/redis$template_number/g" | sed "s/wordpress1/wordpress$template_number/g" >> $newtempfile
	echo "$newtempfile file updated!"
done
cat $newtempfile
echo "**** Done ****"
