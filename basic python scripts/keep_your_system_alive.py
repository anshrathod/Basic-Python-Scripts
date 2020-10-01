"""
Author: Jaqsparow
Purpose: Script to keep your system alive. It takes one argument i.e number of minutes system is to be active 
         and action to be taken after  that no of minutes
Usage: keep_your_system_alive.py -t COUNT -a s|r
example to keep a system active for 30 minutes: keep_your_system_alive.py -t 30
example to keep a system active for 1 hour and then turn off the PC: keep_your_system_alive.py -t 60 -a s
example to keep a system  active for 2 hours and then restart it: keep_your_system_alive.py -t 120 -a r
"""
import argparse
import pyautogui
import time
import os
from PIL import ImageGrab

def timer(n, action):
    counter = 0
    current = time.strftime('%H:%M:%S', time.localtime())
    while n > counter:
        print(f'{n-counter} Minutes to go')
        counter = counter + 1
        time.sleep(60)
        pyautogui.click(button='right')
    date = time.strftime('%d-%b-%Y_%H-%M-%S', time.localtime())
    screenshot = ImageGrab.grab()
    image_location = 'C:\\Users\\jaqsp\\Desktop\\Snapshot\\image_' + date + '.jpeg'
    screenshot.save(image_location)
    if action in ['s', 'S']:
        os.system("shutdown -s -f -t 0")
    if action in ['r', 'R']:
        os.system("Shutdown -r -f -t 0")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Enter time in minutes")
    parser.add_argument("-a", "--action", help="want to shutdown?")

    args = parser.parse_args()
    if args.time:
        timer(int(args.time), args.action)
