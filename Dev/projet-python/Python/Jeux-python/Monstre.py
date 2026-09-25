import pygame


class Monstre(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack= 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/Dracaufeu.png")
        self.image = pygame.transform.scale(self.image, (200, 230))
        self.rect = self.image.get_rect()
        self.rect.x = 1080
        self.rect.y = 450
    def forward(self):
        self.rect.x -= self.velocity