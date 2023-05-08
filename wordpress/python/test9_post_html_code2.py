from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# Set up the WordPress client
wp_url = 'http://en.domain.local/xmlrpc.php'
wp_username = 'admin'
wp_password = 'P@ssw0rd'
client = Client(wp_url, wp_username, wp_password)

# Create a new post
post = WordPressPost()
post.title = 'My New HTML Post 2'
post.content = '<!DOCTYPE html><html><head></head><body><h3>My Audio Player</h3><audio controls><source src="https://github.com/Nima-Yeganeh/Public/raw/main/zprojects/pr3/example.mp3" type="audio/mpeg"></audio></body></html>'
post.post_status = 'publish'

# Publish the post
client.call(NewPost(post))
