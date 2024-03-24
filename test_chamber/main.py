import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
TARGET_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
score = 0


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Tiro ao Alvo")

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TARGET_SIZE, TARGET_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH - TARGET_SIZE), random.randint(0, HEIGHT - TARGET_SIZE))

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

all_sprites = pygame.sprite.Group()
targets = pygame.sprite.Group()
cursor = Cursor()
all_sprites.add(cursor)


for _ in range(5):
    target = Target()
    all_sprites.add(target)
    targets.add(target)

running = True
while running:

    #Se chegar a 10 pontos, acabou!
    print(score)
    if score == 10:
        pygame.quit()
        sys.exit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hits = pygame.sprite.spritecollide(cursor, targets, True) 
            for hit in hits:
                score = score + 1
                new_target = Target()  
                all_sprites.add(new_target)
                targets.add(new_target)

    window.fill(BLACK)  
    all_sprites.update()  
    all_sprites.draw(window)  
    pygame.display.flip()  

pygame.quit()
sys.exit()
