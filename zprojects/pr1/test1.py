import os

original_string1 = __file__
new_string1 = original_string1.replace('test1.py', 'filename1.txt')
file_path1 = new_string1
if os.path.exists(file_path1):
    with open(file_path1, 'r') as file:
        contents = file.read()
#        print(contents)
else:
    print(f"File {file_path1} does not exist.")

original_string2 = __file__
new_string2 = original_string2.replace('test1.py', 'filename2.txt')
file_path2 = new_string2
if os.path.exists(file_path2):
    with open(file_path2, 'r') as file:
        contents = file.read()
#        print(contents)
else:
    print(f"File {file_path2} does not exist.")

original_string3 = __file__
new_string3 = original_string3.replace('test1.py', 'filename3.txt')
file_path3 = new_string3
if os.path.exists(file_path3):
    with open(file_path3, 'r') as file:
        contents = file.read()
#        print(contents)
else:
    print(f"File {file_path3} does not exist.")

with open(file_path2, 'r') as file1, open(file_path1, 'r') as file2, open(file_path3, 'w') as output_file:
    for line1 in file1:
        faqs = []
        file2.seek(0)
        for line2 in file2:
            string = line1.strip() + ' ' + line2.strip()
            faqs.append(string)
        for string in faqs:
            # print(string)
            output_file.write(string + '\n')

with open(file_path3, 'r') as f:
    for line in f:
        print(line.strip())
