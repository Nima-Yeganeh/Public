import urllib.request
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

query = "cats"
num_images = 10
directory = generate_filepath()

# if not os.path.exists(directory):
#     os.makedirs(directory)

url = "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(query)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

html = response.read()

# Parse HTML with BeautifulSoup to extract image URLs
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
img_urls = []
for img in soup.find_all('img'):
    img_urls.append(img.get('src'))

# Download images and save to disk
import uuid

for i, url in enumerate(img_urls[:num_images]):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        filename = os.path.join(directory, str(uuid.uuid4()) + ".jpg")
        with open(filename, 'wb') as f:
            f.write(data)
        print("Downloaded image {} of {}".format(i+1, num_images))
    except:
        print("Error downloading image {} of {}".format(i+1, num_images))
