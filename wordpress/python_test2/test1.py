# python.exe -m pip install --upgrade pip
# pip install --upgrade pip
# pip install python-wordpress-xmlrpc
# pip install --upgrade --force-reinstall python-wordpress-xmlrpc
# pip install openai

import os
import openai
import time
import datetime
import random
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

wp_username = 'admin'
wp_password = 'P@ssw0rd'

xcode = input("What is the code? ")
openai.api_key = "sk-"+xcode+"joeRLSZjsL9bOXI2PT3BlbkFJEc4ys7pAJe7SL82uqxtE"

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

original_string4 = __file__
new_string4 = original_string4.replace('test1.py', 'filename4.txt')
file_path4 = new_string4
if os.path.exists(file_path4):
    with open(file_path4, 'r') as file:
        contents = file.read()
#        print(contents)
else:
    print(f"File {file_path4} does not exist.")

with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2, open(file_path3, 'w') as output_file:
    for line1 in file1:
        faqs = []
        file2.seek(0)
        for line2 in file2:
            string = line1.strip() + ' ' + line2.strip()
            faqs.append(string)
        for string in faqs:
            # print(string)
            output_file.write(string + '\n')

with open(file_path3, 'r') as infile:
    data = [line.strip() for line in infile]
random.shuffle(data)
with open(file_path4, 'w') as outfile:
    for line in data:
        outfile.write(line + '\n')

def generate_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": question},
            ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return(result)

def generate_filename(newfilename):
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), newfilename+'.MD')
    newfile_path1 = new_string1
    return(newfile_path1)

def generate_content(zlanguage, zurl, prompt, sleep_time):
    time.sleep(sleep_time)
    post_title = generate_response("Translate in " + zlanguage + " >> " + prompt)
    # print(post_title)
    story = generate_response(prompt + " >> Answer in " + zlanguage)
    # print(story)
    wp_url = 'http://'+zurl+'/xmlrpc.php'
    client = Client(wp_url, wp_username, wp_password)
    post = WordPressPost()
    post.title = post_title
    post.content = story
    post.post_status = 'publish'
    client.call(NewPost(post))    
    return(post_title)

with open(file_path4, 'r') as f:
    for line in f:
        print('started...')
        # time.sleep(30)
        prompt = line.strip()
        print(prompt)
        story = generate_response(prompt)
        # print(story)
        # with open(generate_filename(prompt), 'w') as output_file:
        # output_file.write(story + '\n')
        zurl = 'domain.local'
        post_title = prompt
        wp_url = 'http://'+zurl+'/xmlrpc.php'
        client = Client(wp_url, wp_username, wp_password)
        post = WordPressPost()
        post.title = post_title
        post.content = story
        post.post_status = 'publish'
        client.call(NewPost(post))
        zurl = 'en.domain.local'
        post_title = prompt
        wp_url = 'http://'+zurl+'/xmlrpc.php'
        client = Client(wp_url, wp_username, wp_password)
        post = WordPressPost()
        post.title = post_title
        post.content = story
        post.post_status = 'publish'
        client.call(NewPost(post))
        print(generate_content("Russian (ru) Language", "ru.domain.local", prompt, 30))
        print(generate_content("Spanish (es) Language", "es.domain.local", prompt, 30))
        print('done!')
        time.sleep(0)
