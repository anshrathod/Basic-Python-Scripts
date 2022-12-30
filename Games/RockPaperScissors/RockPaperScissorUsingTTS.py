from random import randint
import pyttsx3  # Text to speech library for python

# Game Variables
COMP_MOVES = {1: 'R', 2: 'P', 3: 'S'}
SCORE = 0
GAMES = 0
# Initialization of Pyttsx3
engine = pyttsx3.init()


def print_n_say(text):
    """
    This function displays and says the text provided in argument.
    """
    print(text)
    engine.say(text)
    engine.runAndWait()
    return None


print_n_say("Welcome tO ROCK PAPER SCISSOR Game")
print_n_say("******RULES******")
print_n_say("Press 'R' for Rock")
print_n_say("Press 'P' for Paper")
print_n_say("Press 'S' for Scissor")


def take_input():
    """
    Takes a valid input from user.
    """
    while True:
        user_choice = input('ROCK (R) | Paper (P) | Scissor (S):\n').upper()
        if user_choice == 'R' or user_choice == 'P' or user_choice == 'S' or user_choice == 'Q':
            return user_choice
        else:
            print_n_say("Invalid move! Try again")


while True:
    player = take_input()
    GAMES += 1
    computer = COMP_MOVES[randint(1, 3)]
    print(f'Computer: {computer} VS Player: {player}')

    # Specifying winning condition for player and computer based on moves.
    if (player == 'R' and computer == 'P') or (player == 'p' and computer == 's') or (
            player == 'S' and computer == 'R'):
        print_n_say("Computer win")
    elif (player == 'R' and computer == 'S') or (player == 'S' and computer == 'P') or (
            player == 'P' and computer == 'R'):
        print_n_say("You win")
        SCORE += 1
    elif player == 'Q':  # Break the loop if user input 'Q'.
        print_n_say("Thanks for playing")
        print(f"Your score is: {SCORE}/{GAMES}")  # Displaying the game score
        break
    else:
        print_n_say("Game Draw")
    print('Press Q to quit')
