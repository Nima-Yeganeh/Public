import os

def generate_filename(newfilename):
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), newfilename+'.MD')
    newfile_path1 = new_string1
    return(newfile_path1)

print(generate_filename('test'))
