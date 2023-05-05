#!/bin/bash

# This script renames all files in the current directory with a given file extension

file_extension=".txt"

for file in *"$file_extension"; do
    new_file=$(echo "$file" | sed "s/$file_extension/.md/")
    mv "$file" "$new_file"
    echo "Renamed file: $file -> $new_file"
done
