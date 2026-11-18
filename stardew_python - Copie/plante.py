class Plante:    
    
    ETATS = ["graine", "pousse", "plante"]

    def __init__(self, nom ,vitesse ):
        self.nom = nom
        self.niveau_croissance = 0
        self.images = [
            pygame.image.load("assets/sprites/objets/{etat}.jpeg") 
            for etat in self.ETATS
        ]
