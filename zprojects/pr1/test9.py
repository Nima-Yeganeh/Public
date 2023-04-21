import time
import datetime
import os

def generate_filename(newfilename):
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), newfilename+'.txt')
    newfile_path1 = new_string1
    return(newfile_path1)

# open the file for reading
with open(generate_filename('filename3'), 'r') as f:
    # read the first line
    line = f.readline()

    # loop until there are no more lines
    while line:
        # print the current line
        print(line.strip())

        # wait for 5 seconds
        time.sleep(5)

        # read the next line
        line = f.readline()

        # print the current time
        print(datetime.datetime.now())
