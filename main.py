import pygame
import sys
import random

def menu():
    font_title = pygame.font.Font(None, 64)
    font_options = pygame.font.Font(None, 36)

    title_text = font_title.render("Tiro ao Alvo", True, (255, 255, 255))
    start_text = font_options.render("Iniciar Jogo", True, (255, 255, 255))
    quit_text = font_options.render("Sair", True, (255, 255, 255))

    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))

    window.blit(title_text, title_rect)
    window.blit(start_text, start_rect)
    window.blit(quit_text, quit_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(pos):
                    return True
                elif quit_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()

pygame.init()

WIDTH, HEIGHT = 800, 600
TARGET_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Tiro ao Alvo")

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image = pygame.Surface((TARGET_SIZE, TARGET_SIZE))
        self.image.fill(self.color)
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


def criar_alvos():
    for _ in range(8):
        target = Target()
        all_sprites.add(target)
        targets.add(target)


def reiniciar_jogo():
    all_sprites.empty()
    targets.empty()
    cursor.rect.center = (WIDTH // 2, HEIGHT // 2)
    criar_alvos()


def fim_jogo(texto):
    font = pygame.font.Font(None, 64)
    text = font.render(str(texto), True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

pygame.mixer.music.load("parque_de_diversao.mp3")
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)

balloon_pop = pygame.mixer.Sound('balloon_pop.wav')

if not menu():
    pygame.quit()
    sys.exit()

pontuacao = 0
vitoria = 120
font = pygame.font.Font(None, 36)

criar_alvos()

timer = 100
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hits = pygame.sprite.spritecollide(cursor, targets, True)
            for hit in hits:
                new_target = Target()
                all_sprites.add(new_target)
                targets.add(new_target)
                balloon_pop.play()
                pontuacao += 1
            if pontuacao >= vitoria:
                fim_jogo("Você Venceu!")

    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(timer - elapsed_time, 0)

    window.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(window)
    
    text = font.render("Pontuação: " + str(pontuacao), True, WHITE)
    window.blit(text, (10, 10))

    timer_text = font.render("Tempo: " + str(remaining_time), True, WHITE)
    window.blit(timer_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

    if remaining_time <= 0:
        fim_jogo("Fim de Jogo")
