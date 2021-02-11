from random import choice

class Items():

    def __init__(self, element, lalistedepassage):
       
        self.typeobjet = element
        self.tupleposition = choice(lalistedepassage)
        #faire une clef générique pour objet
        self.printvaleur = self.typeobjet["image"]
        self.nomdelobjet = self.typeobjet["name"]
        self.ligne = self.tupleposition[0] 
        self.colonne = self.tupleposition[1]
        self.newtupleposition = (self.ligne*15, self.colonne*15)
        
        


        

        


    