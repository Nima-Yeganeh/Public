#!/bin/bash

# Prompt the user for the lower and higher numbers
echo "Enter the lower number: "
read lower
echo "Enter the higher number: "
read higher

filename="zdatafile.csv"
# Loop through the lines in the file within the specified range
line_number=1
while IFS=',' read -r col1 col2 col3; do
    if (( $line_number >= $lower && $line_number <= $higher )); then
        echo "$col1"
        echo "$col2"
        echo "$col3"
    fi
    (( line_number++ ))
done < $filename
