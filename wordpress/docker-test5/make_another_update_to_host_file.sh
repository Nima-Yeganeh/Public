#!/bin/bash

# Prompt the user for the lower and higher numbers
echo "Enter the lower number: "
read lower
echo "Enter the higher number: "
read higher

filename="zdatafile.csv"
xfile="hostfile.txt"
touch $xfile
rm -f $xfile
line_number=1
while IFS=',' read -r col1 col2 col3; do
    if (( $line_number >= $lower && $line_number <= $higher )); then
        echo "$col1"
        echo "$col2"
        echo "$col3"
        echo "185.223.235.68 "$col3".domain.local" >> $xfile
    fi
    (( line_number++ ))
done < $filename
echo $xfile
cat $xfile

