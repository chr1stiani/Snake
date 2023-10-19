import pygame
import time
import random

pygame.init()

# Nastavení velikosti okna hry
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Barvy
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)

# Velikost a rychlost bloku hada
block_size = 10
snake_speed = 50  # Změněno z 15 na 20 pro ještě pomalejší pohyb

# Font pro zobrazení skóre
font_style = pygame.font.SysFont(None, 50)

def Your_score(score):
    value = font_style.render("Score: " + str(score), True, black)
    window.blit(value, [0, 0])

def our_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], block, block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Pozice hada
    x1 = width / 2
    y1 = height / 2

    # Změna pozice hada
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Pozice ovce
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            window.fill(white)
            message("Prohrál jsi! Stiskni Q-Quit nebo C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, black, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(block_size, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.delay(snake_speed)

    pygame.quit()
    quit()

gameLoop()
