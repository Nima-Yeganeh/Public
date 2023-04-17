import wordpress_xmlrpc
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# Define the WordPress credentials
url = 'http://domain.local/xmlrpc.php'
username = 'admin'
password = 'P@ssw0rd'

# Connect to the WordPress client
client = Client(url, username, password)

# Create a new post
post = WordPressPost()

# Set the post content
post.title = 'Your post title 2'
post.content = 'Your post description'

# Set the post tags
tags = ['tag1', 'tag2', 'tag3']
post.terms_names = {
    'post_tag': tags
}

# Set the post category
category = ['category_name']
post.terms_names = {
    'category': category
}

# Publish the post
post.post_status = 'publish'

# Create the new post on WordPress
post_id = client.call(NewPost(post))

# Print the post ID
print('New post created with ID:', post_id)

# In this example, we're using the wordpress_xmlrpc package to connect to a WordPress site via XML-RPC, which is enabled by default on WordPress installations. We're setting the post title and content using the WordPressPost object, and then setting the tags and category using the terms_names property. Finally, we set the post status to "publish" and create the post using the NewPost method.
