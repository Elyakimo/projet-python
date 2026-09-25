import pygame
#definir une classe pour les projectiles du joueur 2
class Projectile2(pygame.sprite.Sprite):
    #DEFINIR LE CONSTRUCTEUR DE LA CLASSE
    def __init__(self, player2):
        super().__init__()
        self.velocity = 2
        self.player2 = player2
        self.image = pygame.image.load("assets/sonicboom.png")
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player2.rect.x -10
        self.rect.y = player2.rect.y + 40
        self.original_image = self.image
        self.angle = 0
    #DEFINIR LE DEPLACEMENT DU PROJECTILE
    def rotate(self):
        #faire tourner le projectile de 360 degrés
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player2.all_projectiles.remove(self)
    def move(self):
        self.rect.x -= self.velocity
        self.rotate()

            #verifier si le projectile entre en collision avec le joueur 1
        player_group = pygame.sprite.Group(self.player2.game.player)
        for player1 in self.player2.game._check_collision(self, player_group):
            #enlever le projectile
            self.remove()
            #infliger des degats au joueur 1
            player1.damage(self.player2.attack)

        #verifier si le projectile sort de l'ecran
        if self.rect.x<0:
            #detruire le projectile
            self.remove()
            print("projectile detruit")