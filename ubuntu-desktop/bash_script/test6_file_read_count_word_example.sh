#!/bin/bash

# This script reads a file line by line and counts the number of words in each line

file_name="example.txt"

while read -r line; do
  num_words=$(echo "$line" | wc -w)
  echo "Line \"$line\" has $num_words words"
done < "$file_name"
