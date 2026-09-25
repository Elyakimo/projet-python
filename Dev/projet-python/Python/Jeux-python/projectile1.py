import pygame

#definir une classe pour les projectiles du joueur 1
class Projectile1(pygame.sprite.Sprite):

    #DEFINIR LE CONSTRUCTEUR DE LA CLASSE
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load("assets/bill.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 165
        self.rect.y = player.rect.y + 60
        
       
    
    #DEFINIR LE DEPLACEMENT DU PROJECTILE

    def remove(self):
        self.player.all_projectiles.remove(self)
    
    def move(self):
        self.rect.x += self.velocity
        
        #verifier si le projectile entre en collision avec le joueur 2
        player2_group = pygame.sprite.Group(self.player.game.player2)   
        for player2 in self.player.game._check_collision(self, player2_group):
            #enlever le projectile
            self.remove() 
            #infliger des degats au joueur 2
            player2.damage(self.player.attack)           
            

        #verifier si le projectile sort de l'ecran
        if self.rect.x>1080:
            #detruire le projectile
            self.remove()
            print("projectile detruit")