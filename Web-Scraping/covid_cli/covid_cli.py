#!/usr/bin/python3
# Created by Sam Ebison ( https://github.com/ebsa491 )
# If you have found any important bug or vulnerability,
# contact me pls, I love learning ( email: ebsa491@gmail.com )

"""
A script for extracting covid-19 virus online information from (https://www.worldometers.info/coronavirus/)
"""

import sys
import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"

def main():
    """The main function of the script."""
    pass

def send_request(url):
    """
    Sends a GET request to the URL,
    and returns the result (returns -1 for any error).
    - url: The website URL.
    """

    try:
        return requests.get(url)
    except:
        return -1

def parse_result(result):
    """
    Parses the HTML result,
    and returns the info.
    - result: The HTML result (send_request function returns).   
    """
    pass

if __name__ == '__main__':
    main()
