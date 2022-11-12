import pygame
pygame.init()

# Generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'image de notre jeu
background = pygame.image.load("assets/bg.jpg")

running = True

# Boucle tant que cette condition est vrai
while running:

  # appliquer l'arriere plan de notre jeu
  screen.blit(background, (0, -200))

  # mettre à jour l'ecran
  pygame.display.flip()

  # si le joueur ferme cette fenetre
  for event in pygame.event.get():
    # que l'evenement est fermeture de fenetre
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fermeture du jeu")
