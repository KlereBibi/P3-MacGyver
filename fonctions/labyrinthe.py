from fonctions.constantes import MONLABYRINTHE
from fonctions.constantes import ITEMS
from fonctions.macgyver import MacGyver
from fonctions.gardien import Gardien
from random import choice
from fonctions.objets import Items


class Labyrinthe:

    def __init__(self):
        self.malistedetuplemur = []
        self.malistedetuplepassage = []
        self.longueur = 0
        self.largeur = 0
        self.listedobjet = []

    def readlab(self):
        monfichier = open(MONLABYRINTHE, "r")
        i = 0
        for line in monfichier:
            j = 0
            for character in line: 
                if "m" in character:
                    self.malistedetuplemur.append((i,j))
                elif "p"  in character:
                    self.malistedetuplepassage.append((i,j))
                elif "h" in character:
                    self.macgyver = MacGyver(i, j) #accroche à mon objet
                elif "g" in character:
                    self.gardien = Gardien(i, j)
                j+=1
            i += 1
        self.longueur = i 
        self.largeur = j

    def printlab(self):
        #self.choixdelobjet = choice(ITEMS)
        for i in range(self.longueur):
            for j in range(self.largeur):
                for element in self.listedobjet:
                    if (i,j) == element.tupleposition:
                        print(element.printvaleur, end='')
                if (i,j) in self.malistedetuplemur:
                    print("m",end='')
                    
                elif (i,j) in self.malistedetuplepassage:
                    print("p",end='')

                elif i == self.gardien.ligne and j == self.gardien.colonne:
                    print("g",end='') 
                elif i == self.macgyver.ligne and j == self.macgyver.colonne:
                    print("h",end='')
            print("")
                
    def objetdanslabyrinthe(self):
        for element in ITEMS:
            objet = Items(element, self.malistedetuplepassage )
            self.listedobjet.append(objet)
            self.malistedetuplepassage.remove(objet.tupleposition)


            
        
        

        

       
            
            
            
            


            

         

       
            
            

            #generalisation 

    



            
               

            





               
             


     

