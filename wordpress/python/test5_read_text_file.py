import os

# Define the file path
file_path = 'C:/Users/Nima/Desktop/nima_git/Public/wordpress/python/file.txt'

# Check if the file exists
if os.path.isfile(file_path):

    # Open the file
    with open(file_path, 'r') as f:

        # Read the file contents
        file_contents = f.read()

        # Print the file contents
        print(file_contents)
else:
    print('File not found.')

