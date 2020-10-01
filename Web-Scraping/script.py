from bs4 import BeautifulSoup
import requests
import ssl

# ignore the ssl certifiate errors for https
certerr = ssl.ceate_default_context()
certerr.check_hostname = False
certerr.verify_mode = ssl.CERT_NONE

# requesting URL from user to input (respecting the policy of website regarding web-scraping)

url = input('Enter URL : ')

# other functionality can be added here by other contributors :) #HAPPY_HACKATHON
