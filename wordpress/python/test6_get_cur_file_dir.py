import os

# Get the current directory
current_dir = os.getcwd()

# Specify the file path relative to the current directory
file_path = os.path.join(current_dir, 'file.txt')

print(file_path)
filename = os.path.basename(file_path)
print(filename)
