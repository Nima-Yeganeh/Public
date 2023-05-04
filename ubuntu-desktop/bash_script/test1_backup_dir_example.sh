#!/bin/bash

# Define the source and destination directories
src="test1/myfiles"
dst="test1/backup"

# Create the destination directory if it doesn't exist
if [ ! -d "$dst" ]; then
    mkdir "$dst"
fi

# Create a timestamped backup archive
backup_file="$dst/myfiles_$(date +%Y-%m-%d_%H-%M-%S).tar.gz"
tar -czf "$backup_file" "$src"

# Print a message indicating that the backup was successful
echo "Backup created: $backup_file"
