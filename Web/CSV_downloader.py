# This is a simple example of a function that allows to download CSV from the web simply by using it's url. It's usefull when you are preparing examples of any operations based on data.

# Required imports
import requests
import csv

# URLs to data
data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Defining a function that would allow us to download a delimited file.
def downloader_fun(url_str,delim):
    with requests.Session() as s:
        download = s.get(url_str)
        reader = csv.reader(download.content.decode('utf-8').splitlines(), delimiter=delim)
        my_list = list(reader)
        return my_list

# Using function
my_file=downloader_fun(data_url,',')

# Let's check if it works
for row in my_file:
    print(row)