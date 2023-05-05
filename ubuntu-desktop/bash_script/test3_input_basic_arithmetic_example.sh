#!/bin/bash

# This script prompts the user for two numbers and performs some arithmetic

echo "Please enter the first number:"
read num1

echo "Please enter the second number:"
read num2

sum=$((num1 + num2))
difference=$((num1 - num2))
product=$((num1 * num2))
quotient=$((num1 / num2))

echo "The sum of $num1 and $num2 is: $sum"
echo "The difference between $num1 and $num2 is: $difference"
echo "The product of $num1 and $num2 is: $product"
echo "The quotient of $num1 and $num2 is: $quotient"
