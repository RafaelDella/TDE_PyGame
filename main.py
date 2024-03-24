'''Libraries'''
import pygame
import sys
import random
from math import *

'''Setup Window'''
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Shooting At Theme Park')
clock = pygame.time.Clock()

run = True
while run:
    mouse_position = pygame.mouse.get_pos()
    pygame.draw.circle

    if pygame.mouse.get_pressed()[0] == True:
        print("Left Mouse Clicked")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    pygame.display.flip()
    clock.tick(60)
