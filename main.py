import pygame
import sys
from raquete import Raquete
from bola import Bola

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tennis for Two")
clock = pygame.time.Clock()

raquete1 = Raquete(WHITE, 10, 100)
raquete1.rect.x = 20
raquete1.rect.y = SCREEN_HEIGHT / 2 - 50

raquete2 = Raquete(WHITE, 10, 100)
raquete2.rect.x = SCREEN_WIDTH - 30
raquete2.rect.y = SCREEN_HEIGHT / 2 - 50

bola = Bola(WHITE, 10, 10, SCREEN_HEIGHT, SCREEN_WIDTH)
bola.rect.x = SCREEN_WIDTH / 2
bola.rect.y = SCREEN_HEIGHT / 2

all_sprites = pygame.sprite.Group()
all_sprites.add(raquete1, raquete2, bola)

font = pygame.font.Font(None, 36)
cor_texto = WHITE

pontos_jogador1 = 0
pontos_jogador2 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        raquete1.rect.y -= 5
    if keys[pygame.K_s]:
        raquete1.rect.y += 5

    if keys[pygame.K_UP]:
        raquete2.rect.y -= 5
    if keys[pygame.K_DOWN]:
        raquete2.rect.y += 5

    bola.update()

    if raquete1.rect.colliderect(bola.rect):
        bola.velocidade_x = abs(bola.velocidade_x)

    if raquete2.rect.colliderect(bola.rect):
         bola.velocidade_x = -abs(bola.velocidade_x)

    if bola.rect.left <= 0:
        pontos_jogador2 += 1
        print("Jogador 2 pontua!")
        bola.rect.x = SCREEN_WIDTH / 2
        bola.rect.y = SCREEN_HEIGHT / 2

    if bola.rect.right >= SCREEN_WIDTH:
        pontos_jogador1 += 1
        print("Jogador 1 pontua!")
        bola.rect.x = SCREEN_WIDTH / 2
        bola.rect.y = SCREEN_HEIGHT / 2

    placar_texto = font.render(f"Jogador 1: {pontos_jogador1}  Jogador 2: {pontos_jogador2}", True, cor_texto)
    placar_rect = placar_texto.get_rect()
    placar_rect.center = (SCREEN_WIDTH // 2, 20)

    raquete1.rect.y = max(0, min(raquete1.rect.y, SCREEN_HEIGHT - raquete1.rect.height))
    raquete2.rect.y = max(0, min(raquete2.rect.y, SCREEN_HEIGHT - raquete2.rect.height))

    screen.fill(BLACK)
    screen.blit(placar_texto, placar_rect)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()