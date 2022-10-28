import re
from bs4 import BeautifulSoup
import requests

HEADER = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def get_titles(link):
    response = requests.get(link, headers=HEADER)
    soup = BeautifulSoup(response.text, "html.parser")

    pattern_title = re.compile(r'"title":{"runs":\[{"text":"(.*?)"}\],"accessibility"') #* catch title

    for match in pattern_title.finditer(soup.prettify()):
        print(match.group(1))

while True:
    link = str(input('yt playlist link: '))
    try:
        get_titles(link)
        break
    except:
        print("invalid link")