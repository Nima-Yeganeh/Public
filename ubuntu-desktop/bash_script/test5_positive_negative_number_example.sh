#!/bin/bash

# This script checks if a number is positive, negative, or zero

echo "Please enter a number:"
read num

if [ $num -gt 0 ]; then
  echo "$num is a positive number"
elif [ $num -lt 0 ]; then
  echo "$num is a negative number"
else
  echo "$num is zero"
fi
