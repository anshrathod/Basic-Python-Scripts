"""
Author: Kartikay Chiranjeev Gupta
Last Modified: 30/12/2022
"""

import random

elements = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
winning_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
user_move = []
comp_move = []


def print_board(elements_):
    """
    Prints the 'X' and 'O' in proper game format.
    :param elements_: List of 'X' and 'O'
    :return: None
    """
    elements_ = iter(elements_)
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(next(elements_), end='|')
            else:
                print(next(elements_))
        if i != 2:
            print('---|---|---')


def take_input():
    """
    Takes a valid input from user.
    :return: int between 1 and 9 as per entered by user.
    """
    position = input("Select position: ")
    invalid = True
    while invalid:
        try:
            position = int(position)
            if 1 <= position <= 9 and position not in user_move and position not in comp_move:
                invalid = False
                user_move.append(position)
                elements[position-1] = ' X '
                return position
            else:
                print("Invalid position entered!")
                position = input('Enter a valid position: ')
                continue
        except ValueError:
            print('Invalid character entered!')
            position = input('Enter a valid character: ')
            continue


def random_number():
    """
    Generates a valid random number between 1 to 9.
    :return: int between 1-9.
    """
    if '   ' in elements:
        while True:
            position = random.randint(1, 9)
            if position not in user_move and position not in comp_move:
                comp_move.append(position)
                elements[position-1] = ' O '
                return position
            else:
                continue
    else:
        return comp_move[-1]


def is_winning(move, _name):
    """
    Checks if a player is winning the game.
    :param move: List of all moves entered by player.
    :param _name: Name of Player.
    :return: Bool
    """
    for combo in winning_combo:
        if combo[0] in move:
            if combo[1] in move:
                if combo[2] in move:
                    print('***********')
                    print_board(elements)
                    print('***********')
                    print(f'{_name} Won!!')
                    return True
                else:
                    continue
            else:
                continue
        else:
            continue
    return False


def is_draw(_elements):
    """
    Checks if the game is draw.
    :param _elements: List of all 'X' and 'O'.
    :return: Bool
    """
    if '   ' in _elements:
        return False
    else:
        print("!!DRAW!!")
        return True


if __name__ == '__main__':
    name = input('********** Welcome ************\nEnter your name: ')
    while not (is_winning(user_move, name) or is_winning(comp_move, 'Computer') or is_draw(elements)):
        print_board(elements)
        pos_x = take_input()
        pos_o = random_number()
