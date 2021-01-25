from random import choice

class Items():

    def __init__(self, element, lalistedepassage):
       
        self.typeobjet = element
        self.tupleposition = choice(lalistedepassage)
        #faire une clef générique pour objet
        self.printvaleur = self.typeobjet["image"]
        self.nomdelobjet = self.typeobjet["name"]
        

        
        


        

        


    