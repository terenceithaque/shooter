import pygame

from game import Game
from player import Player

pygame.init()



    






# Generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'image de notre jeu
background = pygame.image.load("assets/bg.jpg")

# charger notre jeu
game = Game()


running = True

# Boucle tant que cette condition est vrai
while running:

  # appliquer la  fenetre du jeu
  screen.blit(background, (0, -200))


  
# appliquer l'image de mon joueur
  screen.blit(game.player.image, game.player.rect)


# verifier si le joueur souhaite aller à gauche ou à droite
  if game.pressed.get(pygame.K_RIGHT):
    game.player.move_right()

  elif game.pressed.get(pygame.K_LEFT):
    game.player.move_left()   

  # mettre à jour l'ecran
  pygame.display.flip()

  # si le joueur ferme cette fenetre
  for event in pygame.event.get():
    # que l'evenement est fermeture de fenetre
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fermeture du jeu")
    # detecter si un joueur lache une touche du clavier
    elif event.type == pygame.KEYDOWN:
      game.pressed[event.key] = True
    elif event.type == pygame.KEYUP:
      game.pressed[event.key] = False



