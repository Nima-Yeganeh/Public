# pip install beautifulsoup4
# sudo apt-get install python-bs4  # for Debian/Ubuntu-based systems
# brew install beautifulsoup4      # for macOS
# pip install googlesearch-python
# pip install --upgrade googlesearch-python

import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

# define the search query
query = 'cute puppies'

# set the number of images to download
num_images = 10

# search for images
url_list = []
for url in search(query, stop=num_images):
    url_list.append(url)

# download the images
for i, url in enumerate(url_list):
    # get the HTML content of the page
    html_content = requests.get(url).text

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # find the image element and get the source URL
    img_tags = soup.find_all('img')
    img_url = None
    for tag in img_tags:
        if 'src' in tag.attrs:
            img_url = tag.attrs['src']
            break

    # download the image
    if img_url is not None:
        img_data = requests.get(img_url).content
        with open(generate_filepath()+'puppy{}.jpg'.format(i), 'wb') as f:
            f.write(img_data)
