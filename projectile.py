import pygame

# definir la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

  # definir le constructeur de cette classe
  def __init__(self, player):
    super().__init__()
    self.velocity = 5
    self.image = pygame.image.load("assets/projectile.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = player.rect.x + 120
    self.rect.y = player.rect.y + 80

   