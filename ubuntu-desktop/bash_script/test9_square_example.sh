#!/bin/bash

# This script prints the squares of the numbers from 1 to 10

for (( i=1; i<=10; i++ )); do
  square=$((i*i))
  echo "The square of $i is $square"
done
