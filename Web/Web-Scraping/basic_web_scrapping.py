# Web scrapping

import requests
url="https://comicvine1.cbsistatic.com/uploads/scale_small/3/31666/4956367-invim2015001-maleevvar-d8a38.jpg"
data=requests.get(url)

# print(data.content)
# print(data.status_code)

with open("file.jpeg","wb") as f:
    f.write(data.content)

url2="http://cb.lk/speech"
data1=requests.get(url2)
speech=data.text
# wb=write binary
with open("PM.txt","wb") as f:
    f.write(data1.content)


import time
time.sleep(2)
# 4 is the user id of the facebook reader
fb_url="http://graph.facebook.com/4/picture?type=large"
data=requests.get(fb_url)
with open("mark.jpeg","wb") as f:
    f.write(data.content)

fb_url="http://graph.facebook.com/{}/picture?type=large"
for i in range(4,21):
    # print(fb_url.format(i))
    data=requests.get(fb_url.format(i))
    with open("{}.jpeg".format(i),"wb") as f:
        f.write(data.content)
    

# Beautiful soup
from bs4 import BeautifulSoup
url="https://www.passiton.com/inspirational-quotes?page=2"
data=requests.get(url)
soup=BeautifulSoup(data.text)
# print(soup)
# soup.prettify
# this will give title in html
print(soup.title)
print(soup.title.string)
# a for anchor tag
# img for image tag
# it will give only first anchor ag
# soup.a
# soup.img
# this will give all image tags
all_img=soup.find_all("img")
# src tag is inside the image tag
# all_img[5]['src']
count =1
for i in all_img:
    link=i['src']
    # this will print links of all images
    # this if else condition will remove the assets/...
    # and link.find("monday")!=-1
    if link.find("https")==-1:
        # -1 stands for false
        continue
    else:
        print(link)
        data=requests.get(link)
        with open("{}.jpeg".format(count),"wb") as f:
            f.write(data.content)
        count+=1
