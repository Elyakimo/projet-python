import pygame
from player import Player
from player2 import Player2

#creer une seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        #generer notre joueur
        self.player = Player(self)
        self.player2 = Player2(self)
        self.pressed = {}

    def _check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)