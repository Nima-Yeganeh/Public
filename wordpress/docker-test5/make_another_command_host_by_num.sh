#!/bin/bash

# Prompt the user for the lower and higher numbers
echo "Enter the lower number: "
read lower
echo "Enter the higher number: "
read higher

filename="zdatafile.csv"
tempfile="commands_host_ver3_temp"
line_number=1
while IFS=',' read -r col1 col2 col3; do
    if (( $line_number >= $lower && $line_number <= $higher )); then
        echo "$col1"
        echo "$col2"
        echo "$col3"
        cat $tempfile | sed "s/docker-test5-wordpress1/docker-test5-wordpress"$col1"/g" | sed "s/domain.local/"$col3"domain.local/g" >> "commands_host"$col1"_ver3.sh"
    fi
    (( line_number++ ))
done < $filename

