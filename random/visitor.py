import webbrowser
import time
import keyboard

count = x # number of times you want to open a tab
secs = x # time after which a tab is to be closed

url = 'xyz'

for _ in range (count):
    # opens a new tab
    webbrowser.open(url, new=0)
    # closes the tab after some time
    time.sleep(secs)
    keyboard.press_and_release('Ctrl + W')