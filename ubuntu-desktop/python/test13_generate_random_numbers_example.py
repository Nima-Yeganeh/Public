import random

# Generate a random integer between 1 and 100
num = random.randint(1, 100)

# Print the random number
print("Random number:", num)

# Generate a random float between 0 and 1
flt = random.random()

# Print the random float
print("Random float:", flt)

# Generate a list of 5 random integers between 1 and 10
lst = random.sample(range(1, 11), 5)

# Print the list of random integers
print("List of random integers:", lst)
