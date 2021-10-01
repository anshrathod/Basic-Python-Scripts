from bs4 import BeautifulSoup
import requests

# creating empty list
urls = []
 
# function created

def Scrape(site):
    # getting the request from url
    r = requests.get(site)

    # converting text

    s = BeautifulSoup(r.text,"html.parser")
    for i in s.find_all("a"):
        href = i.attrs['href']
        if href.startswith("/"):
            site = site + 'href'
            if site not in urls:
                urls.append(site)
                print(site)

                # calling function via recursion
                Scrape(site)

# main function
if __name__ == "__main__":
    site = "https://www.linkedin.com//"
    Scrape(site)