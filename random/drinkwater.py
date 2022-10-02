import time
from plyer import notification 


if __name__ == "__main__":
    while True:
        notification.notify(
        title = " Hi Sanjay , Time to drink water",
        message = " Drinking water is very important to keep our body hydrated , so please keep drinking water. Water is very important for our body .",
        app_icon =r"C:\Users\User\Pictures\icon.ico",
        timeout=20 
      )
    time.sleep(0)