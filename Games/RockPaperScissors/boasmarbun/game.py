'''
    File name: game.py
    Author: boasmarbun (https://github.com/boasmarbun)
    Date created: 02/10/2020
    Python Version: 3.7
'''

import sys, random
wins = 0
losses = 0
ties = 0

def start():  
    while True:    
        checkInput()
        play()

def checkInput():
    while True:
        main_action = input('Press "p" to play or "s" to view the scoreboard, or x to exit the game: ')
        if(main_action == 'x'):
            print("Thank you for playing the game!")
            sys.exit()
        elif(main_action == 's'):
            showScoreboard()
        elif(main_action == 'p'):
            break
        else:
            print("Wrong action")

def showScoreboard() :
    print()
    print('===== Scoreboard =====')
    print('Wins:', wins)
    print('Losses:', losses)
    print('Ties:', ties)
    print('======================')
    print()

def play():    
    player_move = get_player_move()
    computer_move = get_computer_move()
    updateScoreboard(player_move, computer_move)

def get_player_move():
    move = input('Please pick a move, press "r" for rock, press "p" for paper, or "s" for scissors : ')
    validate_player_move(move)
    print_player_move(move)
    return move

def get_computer_move():
    computer_choices = ['r', 'p', 's']
    computer_move = random.choice(computer_choices)
    print_computer_move(computer_move)
    return computer_move

def updateScoreboard(player_move, computer_move):
    global ties
    if(player_move == computer_move):
        print("It's a tie!")
        ties += 1
    elif(player_move == 'r'):
        if(computer_move == 'p'):
            player_lose()
        else:
            player_wins()
    elif(player_move == 'p'):
        if(computer_move == 'r'):
            player_wins()
        else:
            player_lose()
    else:
        if(computer_move == 'p'):
            player_wins()
        else:
            player_lose()

def player_wins():
    global wins
    print("You win!")
    wins += 1

def player_lose():
    global losses
    print("You lose!")
    losses +=1
        
def print_player_move(move):
    if(move == 'p'):
        print('You choose PAPER and ..')
    elif(move == 'r'):
        print('You choose ROCK and ..')
    else:
        print('You choose SCISSOR and ..')

def validate_player_move(move):
    if(not (move == 'r' or move == 'p' or move == 's')):
        print("invalid move")
        get_player_move()

def print_computer_move(computer_move):
    if(computer_move == 'p'):
        print('Computer choose PAPER!')
    elif(computer_move == 'r'):
        print('Computer choose ROCK!')
    else:
        print('Computer choose SCISSOR!')

print('==========================================')
print('Hi! Welcome to the RockPaperScissors game.')
print('==========================================')
print()

start()