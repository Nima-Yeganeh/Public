#!/bin/bash

filename="zdatafile.csv"
# Loop through the lines in the file
while IFS=',' read -r col1 col2 col3; do
	echo "Column 1: $col1"
	echo "Column 2: $col2"
	echo "Column 3: $col3"
done < $filename

