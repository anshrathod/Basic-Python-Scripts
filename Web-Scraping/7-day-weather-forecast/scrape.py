import requests
from bs4 import BeautifulSoup
import pandas as pd

n = input("Enter Postal Code >>")

url_lat_long = "https://in.search.yahoo.com/search;_ylt=AwrPhmmmGZxebzkAoxK6HAx.;_ylc=X1MDMjExNDcyMzAwMg" \
               "RfcgMyBGZyAwRncHJpZANxWEgwMnJhR1FBZWlGM01WSmhHaWpBBG5fcnNsdAMwBG5fc3VnZwMxBG9yaWdpbgNpbi5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmw" \
               "DBHFzdHJsAzE5BHF1ZXJ5AzI0MzEyMiUyMHRlbXByYXR1cmUEdF9zdG1wAzE1ODcyODg0OTQ-?fr2=sb-top-in.search&p={}+temprature&fr=sfp&iscqry=".format(n)
               
page = requests.get(url = url_lat_long)
soup = BeautifulSoup(page.content, "html.parser")
find = soup.find(class_ = "main-temp")
find_high_low = find.find(class_ = "temp-ctnt")
find_curr = find.find_all_next(class_ = "currTemp")
curr_loc = soup.find(class_ = "cptn-ctnt")
loc_find = curr_loc.find(class_ = "txt")


print("Your Location : " + str(loc_find.get_text()) + " " + str(curr_loc.find(class_ = "subTxt").get_text()))
print("Today's Highest", find_high_low.find(class_ = "high").get_text())
print("Today's Lowest", find_high_low.find(class_ = "low").get_text())
print("Current Temp ->", find_curr[0].get_text())


find = soup.find(class_ = "compWeatherSectionList vert small yui3-skin-sam bb-1 plr-10 mt-0")
find = soup.find(class_ = "wcards")
find_day = (find.find_all_next(class_ = "day"))
find_condition = (find.find_all_next(class_ = "condtxt"))
find_high = (find.find_all_next(class_ = "high"))
find_low = (find.find_all_next(class_ = "low"))

find_day = [i.get_text() for i in find_day]
find_condition = [i.get_text() for i in find_condition]
find_high = [i.get_text() for i in find_high]
find_low = [i.get_text() for i in find_low]

d = pd.DataFrame({
    'Day' : find_day,
    'Condition' : find_condition,
    'Hoghest Temp.' : find_high,
    "Lowest Temp.": find_low
})

print(d)
