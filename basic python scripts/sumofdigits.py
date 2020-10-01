import sys


i = int(sys.argv[1])
Sum = 0

while(i > 0):
    Reminder = i % 10
    Sum = Sum + Reminder
    i = i //10

print("Sum of the digits: " , Sum)