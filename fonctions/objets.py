from random import choice

class Items():

    def __init__(self, element, lalistedepassage):
       
        self.typeobjet = element
        self.tupleposition = choice(lalistedepassage)
        #faire une clef générique pour objet
        self.printvaleur = self.typeobjet["image"]
        self.nomdelobjet = self.typeobjet["name"]

"""     def afficherlesimages(self):
        if "name" == "aiguille":
            return self.image_item = pygame.image.load("aiguille.png")
        elif "name" == "un tube en plastique":
            return self.image_item = pygame.image.load("tube_plastique.png")
        elif "name" == "de l'ether":
            return self.image_item = pygame.image.load("ether.png") """
        

        
        


        

        


    