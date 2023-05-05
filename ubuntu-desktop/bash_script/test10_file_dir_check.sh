#!/bin/bash

# This script checks if a file or directory exists

echo "Please enter the path to the file or directory:"
read path

if [ -e "$path" ]; then
  echo "$path exists"
else
  echo "$path does not exist"
fi
