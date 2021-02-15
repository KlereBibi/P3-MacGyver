from random import choice

class Items():

    def __init__(self, element, lalistedepassage):
       
        self.typeobjet = element
        self.tupleposition = choice(lalistedepassage)
        #faire une clef générique pour objet
        self.printvaleur = self.typeobjet["image"]
        self.nomdelobjet = self.typeobjet["name"]
        self.vertical = self.tupleposition[0] 
        self.horizontal = self.tupleposition[1]
        self.newtupleposition = (self.horizontal*15, self.vertical*15)
        
        


        

        


    