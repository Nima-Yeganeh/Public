import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Shuffle the characters and select the first "length" characters
    password = ''.join(random.sample(characters, length))

    return password

# Generate a password and print it to the console
password = generate_password(12)
print("Your password is:", password)
