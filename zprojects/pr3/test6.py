# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
# import urllib2
import urllib.request

searchterm = 'vannmelon' # will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Firefox()
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0

# if not os.path.exists(searchterm):
#     os.mkdir(searchterm)

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath("//div[@class='rg_meta']"):
    counter = counter + 1
    print ("Total Count:", counter)
    print ("Succsessful Count:", succounter)
    print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    try:
        req = urllib.request.Request(img, headers={'User-Agent': header})
        raw_img = urllib.request.urlopen(req).read()
        # File = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
        # File.write(raw_img)
        # File.close()
        succounter = succounter + 1
    except:
            print ("can't get img")

print (succounter, "pictures succesfully downloaded")
browser.close()
