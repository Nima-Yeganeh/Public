#!/bin/bash

# This script performs different actions based on the value of a variable

echo "Please enter a value (a, b, or c):"
read value

case $value in
  a)
    echo "You entered a"
    ;;
  b)
    echo "You entered b"
    ;;
  c)
    echo "You entered c"
    ;;
  *)
    echo "Invalid input"
    ;;
esac
