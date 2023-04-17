import os
import wordpress_xmlrpc
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.media import UploadFile
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.compat import xmlrpc_client

# Define the WordPress credentials
url = 'http://domain.local/xmlrpc.php'
username = 'admin'
password = 'P@ssw0rd'

# Connect to the WordPress client
client = Client(url, username, password)

# Create a new post
post = WordPressPost()

# Set the post content
post.title = 'Your post title 3'
post.content = 'Your post description'

# Set the post tags
tags = ['tag1', 'tag2', 'tag3']
post.terms_names = {
    'post_tag': tags
}

# Set the post category
category = ['Test Category 3']
post.terms_names = {
    'category': category
}

# Upload the image file
image_path = 'C:/Users/Nima/Desktop/nima_git/Public/wordpress/python/file1.jpg'
with open(image_path, 'rb') as img:
    data = img.read()
filename = os.path.basename(image_path)
file = {'name': filename, 'type': 'image/jpeg', 'bits': xmlrpc_client.Binary(data)}
response = client.call(UploadFile(file))

# Set the image as the featured image of the post
post.thumbnail = response['id']

# Publish the post
post.post_status = 'publish'

# Create the new post on WordPress
post_id = client.call(NewPost(post))

# Print the post ID
print('New post created with ID:', post_id)

# In this updated version, we've added the ability to upload an image file to the WordPress site using the UploadFile method. We open the image file using a with statement, read the binary data, and then use the os.path.basename function to get the filename. We then call the UploadFile method with the filename and data, and store the response. Finally, we set the thumbnail property of the post to the ID of the uploaded image, and create the post as before.

