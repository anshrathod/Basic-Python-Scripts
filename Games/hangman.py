import random
import sys

list_words = ["hello", "computer", "python", "java", "html", "world", "apple", "windows"]

guessed_word = []
random_word = random.choice(list_words)
word_length = len(random_word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []


def intro():
    print("\tHello and Welcome to Hangman (A word prediction game)")

    while True:
        name = input("Enter your name:\n").strip()
        if name == "":
            print("Enter a valid name\n")
        else:
            break
    print("\n\t\tSo %s  welcome to the Game :) " % name)


intro()


def game():
    while True:
        string = input("So you ready to play :\n ")
        if string == "yes" or string == "Y" or string == "y":
            break
        elif string == "No" or string == "N" or string == "n":
            sys.exit()
        else:
            print("Please Enter something ")
            continue


game()


def rules():
    for _ in random_word:
        guessed_word.append("_")

    print("Ok, so the word You need to guess has", word_length, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guessed_word)


def guessing():
    guess_no = 1
    while guess_no < 10:
        guess = input("\nPick a letter : ")
        if guess not in alphabet:
            print("pick a letter from a-z ")

        elif guess in letter_storage:
            print("Already guessed this letter.")
        else:

            letter_storage.append(guess)
            if guess in random_word:
                print("You guessed correctly")
                for x in range(0, word_length):
                    if random_word[x] == guess:
                        guessed_word[x] = guess
                print(guessed_word)
                if '_' not in guessed_word:
                    print("You won")
                    break
            else:
                print("Guessed letter not in the word")
                guess_no += 1
                if guess_no == 10:
                    print("Sorry, you have used all your chances. YOU LOST !!")


rules()
guessing()

print("\tGAME OVER !! ")

# By: Darsh Asawa (https://github.com/DarshAsawa)
