from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk() # FUCTION FROM TKINTER FOR GUI
root.title("Digital Clock") #TITLE OF CLOCK

def time():
    string = strftime('%H:%M:%H:%S %p') #TIME FORMATE
    label.config(text=string) #DIPLAY TIME
    label.after(1000, time) #AFTER 1 SEC RELOAD

label = Label(root, font=("ds-digital" , 80), background = "black", foreground="cyan") 
label.pack(anchor='center')

time()

mainloop()