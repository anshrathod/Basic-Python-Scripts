#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
from requests.utils import quote

argc = len(sys.argv)
if argc < 2:
    print("usage:\n./mal.py <anime keyword>")
    exit()

keyword = " ".join(sys.argv[1:])
url = f"https://myanimelist.net/anime.php?q={quote(keyword)}"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find_all("table")
rows = table[2].find_all("tr")[1:]

i = 0
maxcontent = 5
for row in rows:
    if i == 0:
        pass
    elif i > maxcontent:
        break
    i += 1
    data = row.find_all("td")
    title = data[0].find("img")["alt"]
    show_type = data[2].string.strip()
    episode = data[3].string.strip()
    score = data[4].string.strip()
    print("=====================")
    print("title:", title)
    print("show type:", show_type)
    print("number of episode:", episode)
    print("score:", score)
    print("=====================\n\n")
