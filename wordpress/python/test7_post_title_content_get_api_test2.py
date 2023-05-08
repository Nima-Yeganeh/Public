# python.exe -m pip install --upgrade pip
# pip install --upgrade pip
# pip install python-wordpress-xmlrpc
# pip install --upgrade --force-reinstall python-wordpress-xmlrpc
# pip install openai
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import openai

xcode = input("What is the code? ")
# print("Code: " + xcode + "")

openai.api_key = "sk-"+xcode+"joeRLSZjsL9bOXI2PT3BlbkFJEc4ys7pAJe7SL82uqxtE"

zurl = 'en.domain.local'
post_title = "Why should DevOps engineer learn kubernetes?"

wp_url = 'http://'+zurl+'/xmlrpc.php'
wp_username = 'admin'
wp_password = 'P@ssw0rd'

def generate_content(topic):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": topic},
            ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return(result)

client = Client(wp_url, wp_username, wp_password)
post = WordPressPost()
post.title = post_title
post.content = generate_content(post_title)
post.post_status = 'publish'
client.call(NewPost(post))
