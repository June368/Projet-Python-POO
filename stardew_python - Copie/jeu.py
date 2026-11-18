import pygame
from joueur import Joueur
from terrain import Terrain
from plante import Plante

class Jeu :
    def __init__(self):
        
        self.player = Joueur()                               #générer le joueur
        self.pressed = { }

        self.largeur = 1280
        self.hauteur =  720
        # test implementation du champ
        self.champ = Terrain(500, 450, 200, 150, champ) 
        newplante = Plante("blé", 5)
        self.champ.planter(0, 0, newplante)
    def move(self):
        
         

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < self.largeur- self.player.rect.width:
            self.player.rect.x += 2
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0 :
            self.player.rect.x -= 2
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 0 : 
            self.player.rect.y -= 2
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y < self.hauteur - self.player.rect.height : 
            self.player.rect.y += 2 


    def run(self) : 
        running = True
        ecran = pygame.display.set_mode((self.largeur, self.hauteur)) 


                            #taille de l'écran
        pygame.display.set_caption("Stardew Valley")                       #renommer la fenetre  
        background = pygame.image.load("assets/background.jpg") 
        #jeu = Jeu()          #image de fond
        while running:
 
            ecran.blit(background,(0,0))
            self.champ.afficher(ecran)                                    #affichage du champ et des plantes                              
            ecran.blit(self.player.image,self.player.rect)

            self.move() 
    
            pygame.display.flip()                                          #afficher image de fond      
   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                              #quitter la fenetre 
                    running = False 
                if event.type == pygame.KEYDOWN :
                    self.pressed[event.key] = True                          #la touche est active
                if event.type == pygame.KEYUP :                            #la touche n'est plus utilisée
                    self.pressed[event.key] = False
