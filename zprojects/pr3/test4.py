import urllib.request
import os

query = "cats"
num_images = 10
directory = "cat_images"

if not os.path.exists(directory):
    os.makedirs(directory)

url = "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(query)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

html = response.read()

# Your remaining code here

