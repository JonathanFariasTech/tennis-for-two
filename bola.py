import pygame

class Bola(pygame.sprite.Sprite):
    def __init__(self, color, width, height, screen_height, screen_width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocidade_x = 5
        self.velocidade_y = 5
        self.screen_height = screen_height
        self.screen_width = screen_width

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.velocidade_x = -self.velocidade_x

        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.velocidade_y = -self.velocidade_y