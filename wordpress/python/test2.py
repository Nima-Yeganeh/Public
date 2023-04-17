from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# Set up the WordPress client
wp_url = 'http://domain.local/xmlrpc.php'
wp_username = 'your_wordpress_username'
wp_password = 'your_wordpress_password'
client = Client(wp_url, wp_username, wp_password)

# Create a new post
post = WordPressPost()
post.title = 'Your post title'
post.content = 'Your post content'
post.post_status = 'publish'

# Publish the post
client.call(NewPost(post))

# In this code, you first set up the WordPress client by specifying the WordPress URL, username, and password. Then you create a new WordPressPost object and set its properties, such as the title, content, and post status. Finally, you call the NewPost method of the client and pass in the WordPressPost object to publish the post.

# Note that you need to have the wordpress-xmlrpc library installed in your Python environment. You can install it using pip:
# python.exe -m pip install --upgrade pip
# pip install --upgrade pip
# pip install python-wordpress-xmlrpc
# pip install --upgrade --force-reinstall python-wordpress-xmlrpc
