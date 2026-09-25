import pygame
from game import Game
pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption("Binks2Binks")
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
# importer le fond de notre jeu
background = pygame.image.load("assets/fond.png")

#charger notre jeu
game = Game()
running = True
#boucle tant que c'est vrai la fenetre ne se ferme pas
while running:

    #appliquer le fond de notre jeu
    screen.blit(background, (-150, 0))

    #appliquer notre personnage
    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.player2.image, game.player2.rect)

    #afficher les barres de vie
    game.player.update_health_bar(screen)
    game.player2.update_health_bar(screen)

    #Deplacer et afficher les projectiles du joueur 1
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    #Deplacer et afficher les projectiles du joueur 2
    for projectile in game.player2.all_projectiles:
        projectile.move()
    #Afficher les projectiles du joueur 1
    game.player.all_projectiles.draw(screen)
    #Afficher les projectiles du joueur 2
    game.player2.all_projectiles.draw(screen)
    
    #verifier les degats
    game.player.damage(10)
    game.player2.damage(10)
    
    #verifier le deplacement du joueur 1
    if game.pressed.get(pygame.K_d) and game.player.rect.x < 1080 - game.player.rect.width:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_z):
        game.player.jump()
    #verifier le deplacement du joueur 2
    if game.pressed.get(pygame.K_RIGHT) and game.player2.rect.x < 1080 - game.player2.rect.width:
        game.player2.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player2.rect.x > 0:
        game.player2.move_left()
    if game.pressed.get(pygame.K_UP):
        game.player2.jump()
    #appliquer la gravite
    game.player.apply_gravity()  
    game.player2.apply_gravity()

    #mettre a jour le contenu de notre fenetre
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fin des sayans")
        #detecter si une touche du clavier est appuyee
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est appuyee pour le joueur 1
            if event.key == pygame.K_SPACE:
                game.player.lancer_projectile()
            #detecter si la touche entree est appuyee pour le joueur 2
            if event.key == pygame.K_RETURN:
                game.player2.lancer_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False