import pygame
import random
import sys
import time
import os
from pygame.locals import *

"""
Author: Kartikay Chiranjeev Gupta
Last Modified: 30/12/2022
"""
"""SNAKE GAME"""


def snake_display(win, colour, b_p_list):
    """
    Draws snake body based on coordinates.
    """
    for x, y in b_p_list:
        s_x = x
        s_y = y
        pygame.draw.rect(win, colour, (s_x, s_y, 10, 10))


def crash(s_x, s_y, sound):
    """
    Checks the crashing condition and plays the crash sound.
    """
    if s_x <= -5 or s_x >= 1200:
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(1)
        time.sleep(0.5)
        return True
    elif s_y <= -5 or s_y >= 600:
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(1)
        time.sleep(0.5)
        return True
    return False


def screen_text(win, text, font1, size, boolean, x, y, a, b, c):
    """
    Renders the text on screen.
    """
    font = pygame.font.SysFont(font1, size, boolean)
    screen_t = font.render(text, True, (a, b, c))
    win.blit(screen_t, (x, y))


def food_pos_generator():
    """
    Generate random coordinates for fruit.
    """
    x = random.randrange(20, 480)
    y = random.randrange(20, 480)
    return x, y


def eat_food(s_x, s_y, f_x, f_y, b_p, sound2, sco):
    """
    Checks condition for eating fruit and plays beeping sound if eaten.
    """
    if f_x <= s_x <= f_x + 10:
        if f_y <= s_y <= f_y + 10:
            f_x, f_y = food_pos_generator()
            b_p += 1
            sco += 1
            pygame.mixer.music.load(sound2)
            pygame.mixer.music.play(1)
    return f_x, f_y, b_p, sco


def main_game():
    pygame.init()
    game_win = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Rect Snake")
    pygame.mixer.init()
    food_beep = os.path.join("assets/food_beep.wav")
    crash_beep = os.path.join("assets/crash_beep.wav")
    background = pygame.image.load(os.path.join('assets/snake_background.jpg')).convert_alpha()
    food = pygame.image.load(os.path.join("assets/food_img.png")).convert_alpha()
    clock = pygame.time.Clock()
    snake_x = 100
    snake_y = 100
    snake_x_vel = 0
    snake_y_vel = 0
    body_part = 1
    snake_body = []
    _FPS = 30
    food_x, food_y = food_pos_generator()
    over = False
    score = 0
    while not over:
        game_win.blit(background, (0, 0))
        screen_text(game_win, "Score: ", "arial black", 18, True, 20, 18, 255, 0, 0)
        screen_text(game_win, str(score), "arial", 20, True, 100, 20, 0, 0, 0)
        pygame.draw.line(game_win, (0, 0, 0), (0, 3), (1200, 3), 10)
        pygame.draw.line(game_win, (0, 0, 0), (3, 0), (3, 600), 10)
        pygame.draw.line(game_win, (0, 0, 0), (1195, 0), (1195, 600), 10)
        pygame.draw.line(game_win, (0, 0, 0), (0, 595), (1200, 595), 10)
        snake_display(game_win, (0, 0, 0), snake_body)
        game_win.blit(food, (food_x, food_y))
        pygame.display.update()
        dis_down = False
        dis_up = False
        dis_left = False
        dis_right = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    snake_x_vel = 0
                    snake_y_vel = 0
                if event.key == K_UP:
                    if not dis_up:
                        snake_x_vel = 0
                        snake_y_vel = -10
                        dis_down = True
                        dis_up = False
                        dis_left = False
                        dis_right = False

                if event.key == K_DOWN:
                    if not dis_down:
                        snake_x_vel = 0
                        snake_y_vel = 10
                        dis_up = True
                        dis_right = False
                        dis_left = False
                        dis_down = False
                if event.key == K_RIGHT:
                    if not dis_right:
                        snake_x_vel = 10
                        snake_y_vel = 0
                        dis_left = True
                        dis_right = False
                        dis_down = False
                        dis_up = False
                if event.key == K_LEFT:
                    if not dis_left:
                        snake_x_vel = -10
                        snake_y_vel = 0
                        dis_right = True
                        dis_left = False
                        dis_up = False
                        dis_down = False

        snake_body.append([snake_x, snake_y])
        food_x, food_y, body_part, score = eat_food(snake_x, snake_y, food_x, food_y, body_part, food_beep, score)
        if len(snake_body) > body_part:
            snake_body.pop(0)
        snake_x += snake_x_vel
        snake_y += snake_y_vel
        over = crash(snake_x, snake_y, crash_beep)
        clock.tick(_FPS)


main_game()
