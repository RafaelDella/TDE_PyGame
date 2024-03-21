import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()