#!/bin/bash

# Prompt the user for the lower and higher numbers
echo "Enter the lower number: "
read lower
echo "Enter the higher number: "
read higher

filename="zdatafile.csv"
xfile="map.MD"
line_number=1
while IFS=',' read -r col1 col2 col3; do
    if (( $line_number >= $lower && $line_number <= $higher )); then
    	echo "# "$col2" ("$col3")" >> $xfile
	echo "db"$col1 >> $xfile
	echo "redis"$col1 >> $xfile
	echo "wordpress"$col1 >> $xfile
    fi
    (( line_number++ ))
done < $filename

