import pygame


class Joueur(pygame.sprite.Sprite) :                          # la class en sprite 

    def __init__(self):
        #super().__init__()

        self.image = pygame.image.load('assets/sprites/joueur/testperso.webp')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0
        

    # modifier les coordonnée donc déplacer le joueur
    #def move_right(self):
     #   self.rect.x += 2

    #def move_left(self):
      #  self.rect.x -= 2

    #def move_up(self):
     #   self.rect.y -= 2

    #def move_down(self):
     #  self.rect.y += 2