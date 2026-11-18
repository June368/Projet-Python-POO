class Plante:    
    
    ETATS = ["Graine", "Pousse", "Plante"]

    def __init__(self, nom ,vitesse ):
        self.nom = nom
        self.niveau_croissance = 0