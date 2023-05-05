Here are some examples of how to use the cp command in Linux:

    Copy a file to a new location:
cp file.txt /path/to/new/location/

    Copy a file and rename it in the process:
cp file.txt new_file.txt

    Copy all files in a directory to a new location:
cp /path/to/directory/* /path/to/new/location/

    Copy all files in a directory (including subdirectories) to a new location:
cp -r /path/to/directory/ /path/to/new/location/

    Preserve the original file attributes (permissions, timestamps, etc.) when copying a file:
cp -p file.txt new_file.txt

    Copy only files that are newer than the destination files:
cp -u file.txt /path/to/new/location/
