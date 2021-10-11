# importing the pyttsx library
#import random as randint
from random import randint
import pyttsx3 

# initialisation 
engine = pyttsx3.init() 
print("WELCOME TO ROCK PAPER SCISSOR Game")
engine.say("WELCOME TO ROCK PAPER SCISSOR Game")
print("Here are some rules of Game")
engine.say("Here are some rules of Game")

print("Press r for rock")
engine.say("Press r for rock")

print("press p for paper")
engine.say("press p for paper")

print("press s for scissor")
engine.say("press s for scissor")

engine.runAndWait()

while 1:
    player= input(" ROCK (r),Paper (p),Scissor (s)\n")
    computer = randint(1,3)
    if computer==1:
         computer_ch='r'
    elif computer==2:
        computer_ch='p'
    else:
        computer_ch='s'
    
    print(computer_ch,'VS',player)
    if player=='r' and computer_ch=='p':
        print("computer wins")
        engine.say("computer wins")
        engine.runAndWait()
    elif player=='r' and computer_ch=='s':
         print("you win\n")
         engine.say("you win \n")
         engine.runAndWait()
    elif player=='p' and computer_ch=='r':
        print("you wins")
        engine.say("you win")
        engine.runAndWait()
    elif player=='p' and computer_ch=='s':
         print("computer wins")
         engine.say("computer wins")
         engine.runAndWait()
        
    elif player=='s' and computer_ch=='r':
        print("computer wins")
        engine.say("computer wins")
        engine.runAndWait()
    elif player=='s' and computer_ch=='p':
        print("you wins")
        engine.say("you win")
        engine.runAndWait()
    else:
        print("draw")
        engine.say("draw")
        engine.runAndWait()
 
