import random

roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == 'Y':
    print("Rolled dice: ")
    print(random.randint(1, 6))
    roll_again = input("Roll the dices again?")

