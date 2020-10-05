# Author: Sahil Bairagi
# Requirements: install selenium module using 'pip install selenium' and download chrome driver and add it to the path. That's it
# Note: Don't click anywhere on the webwhatsapp opened by selenium while it's sending message else the script will crash.

from selenium import webdriver
from random import randint

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

driver.maximize_window()


name = input("Enter the name of contact: ")
count = input("How many times you want to send the message (default 1): ")
try:
    count = int(count)
except ValueError:
    count = 1

msg = input("Enter your message")
print(f"About to send: {msg} to {name}\n-- {count} times")
input("\nHit enter after scanning QR Code")

user = driver.find_element_by_xpath(f'//span[@title="{name}"]')
user.click()

messageBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    messageBox.send_keys(msg)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

print("Success")
