# Importing required libraries

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore the ssl certifiate errors for https

certerr = ssl.create_default_context()
certerr.check_hostname = False
certerr.verify_mode = ssl.CERT_NONE

# Requesting URL from user to input (respecting the policy of website regarding web-scraping)

url = input('Enter URL (for eg. http://www.randomwebsite.com) : ')
html = urllib.request.urlopen(url, context=certerr).read()
bs = BeautifulSoup(html, "html.parser")

# Scraping all the 'a' tags on the web page

tags = bs('a')
for tag in tags:
	print('LINK : ', tag.get('href', None))
