import pygame

class Terrain():
	def __init__(self,largeur,longeur,posx,posy,spritename):
		#taille et position relative
		self.largeur = largeur
		self.longeur = longeur
		self.posx = posx
		self.posy = posy
		self.sprite = pygame.image.load('assets/sprites/terrain/{spritename}.png')
		self.grid = [
            [
                {
                    "plante": None,
                }
                for x in range(largeur)
            ]
            for y in range(longeur)
        ]