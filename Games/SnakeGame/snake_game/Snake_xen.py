# Developer: Sahil Bairagi(Sahil-k1509)

import pygame
from random import randint, randrange
from time import sleep

pygame.init()
win_max_x, win_max_y = 800, 600
GameDisplay = pygame.display.set_mode((win_max_x, win_max_y))
pygame.display.set_caption("SnakeXenia")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Ariel", 30, True)


def text_centre(msg):
    textSurface = font.render(msg, True, (255, 0, 0))
    return textSurface, textSurface.get_rect()


def screen_print(message):
    text_surf, text_rect = text_centre(message)
    # screen_text = font.render(message, True, (255, 0, 0))
    # GameDisplay.blit(screen_text, [int(win_max_x / 2) - len(message), int(win_max_y / 2)])
    text_rect.center = win_max_x/2, win_max_y/2
    GameDisplay.blit(text_surf, text_rect)

def show_score(score):
    screen_text = font.render("Score: "+str(score), True, (0, 0, 0))
    GameDisplay.blit(screen_text, [win_max_x - 200, 20])


'''
class apple_obj(object):
    def __init__(self, apple_x, apple_y, apple_width):
        self.apple_x = apple_x
        self.apple_y = apple_y
        self.apple_width = apple_width
        self.visible = False

    def draw_apple(self):
        pygame.draw.rect(GameDisplay, (255, 0, 0), [self.apple_x, self.apple_y, self.apple_width, self.apple_width])
        self.visible = True
'''

apple = pygame.image.load("apple.png")
def draw_apple(apple_x, apple_y, apple_width):
    GameDisplay.blit(apple, (apple_x,apple_y))
#    pygame.draw.rect(GameDisplay, (255, 0, 0), [apple_x, apple_y, apple_width, apple_width])


global direction
direction = "right"
img = pygame.image.load("snake_head.png")
def snake(snake_list, snake_width):
    global direction
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    elif direction == "left":
        head = pygame.transform.rotate(img, 90)
    elif direction == "up":
        head = pygame.transform.rotate(img, 0)
    elif direction == "down":
        head = pygame.transform.rotate(img, 180)

    GameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for XnY in snake_list[:-1]:
        pygame.draw.rect(GameDisplay, (0, 124, 0), [XnY[0], XnY[1], snake_width, snake_width])


def gameloop():

    snake_head_x = randint(int(win_max_x / 4), int(3 * win_max_x / 4))
    snake_head_y = randint(int(win_max_y / 4), int(3 * win_max_y / 4))

    snake_velocity = 20
    snake_width = 20
    snake_head_change_x = 0
    snake_head_change_y = 0

    apple_x = round(randrange(0, win_max_x - 40) / 10.0) * 10.0
    apple_y = round(randrange(0, win_max_y - 40) / 10.0) * 10.0
    apple_width = 30

    snake_list = []
    snakelength = 1

    score = 0
    global direction

    ping = 100
    gameover = False
    run = True
    while run:
        pygame.time.delay(ping)

        while gameover:
            GameDisplay.fill((255, 255, 255))
            screen_print("GAME OVER! Q to quit, P to play again")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_p:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_head_change_x == 0:
                    direction = "left"
                    snake_head_change_x = -snake_velocity
                    snake_head_change_y = 0
                elif event.key == pygame.K_RIGHT and snake_head_change_x == 0:
                    direction = "right"
                    snake_head_change_x = snake_velocity
                    snake_head_change_y = 0
                elif event.key == pygame.K_UP and snake_head_change_y == 0:
                    direction = "up"
                    snake_head_change_y = -snake_velocity
                    snake_head_change_x = 0
                elif event.key == pygame.K_DOWN and snake_head_change_y == 0:
                    direction = "down"
                    snake_head_change_y = snake_velocity
                    snake_head_change_x = 0
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake_head_x -= 10
        if keys[pygame.K_RIGHT]:
            snake_head_x += 10
        '''
        if not gameover:
            GameDisplay.fill((255, 255, 255))
            show_score(score)
            draw_apple(apple_x, apple_y, apple_width)

        if 0 < snake_head_x < win_max_x - 10:
            if 0 < snake_head_y < win_max_y - 10:
                snake_head_x += snake_head_change_x
                snake_head_y += snake_head_change_y

        snake_head = [snake_head_x, snake_head_y]
        snake_list.append(snake_head)

        if len(snake_list) > snakelength:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                GameDisplay.fill((255, 255, 255))
                screen_print("Collided into yourself. Game Over!")
                pygame.display.update()
                sleep(1)
                gameover = True

        if not gameover:
            snake(snake_list, snake_width)

        if snake_head_x <= 0 or snake_head_x >= win_max_x - 10 or snake_head_y <= 0 or snake_head_y >= win_max_y - 10:
            gameover = True

        if apple_x - apple_width <= snake_head_x <= apple_x + apple_width:
            if apple_y - apple_width <= snake_head_y <= apple_y + apple_width:
                apple_x = round(randrange(0+100, win_max_x-40) / 10.0) * 10.0
                apple_y = round(randrange(0+100, win_max_y-40) / 10.0) * 10.0
                snakelength += 1
                score += 10
                if ping >= 5:
                    ping = ping - 5

        pygame.display.update()  # same as pygame.display.flip();

        clock.tick(30)

    pygame.quit()
    quit()

gameloop()
