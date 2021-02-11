from fonctions.constantes import MONLABYRINTHE
from fonctions.constantes import ITEMS
from fonctions.constantes import IMAGE_MUR
from fonctions.constantes import IMAGE_PASSAGE
from fonctions.constantes import IMAGE_ETHER
from fonctions.constantes import IMAGE_TUBEENPLASTIQUE
from fonctions.constantes import IMAGE_AIGUILLE
from fonctions.constantes import IMAGE_MACGYVER
from fonctions.constantes import IMAGE_GARDIEN
from fonctions.macgyver import MacGyver
from fonctions.gardien import Gardien
from random import choice
from fonctions.objets import Items
import pygame
pygame.init()

pygame.display.set_caption("Macgyver")
#screen = pygame.display.set_mode((225, 225))#largeur, hauteur ouf


class Labyrinthe:

    def __init__(self):
        self.malistedetuplemur = []
        self.malistedetuplepassage = []
        self.longueur = 0
        self.largeur = 0
        self.listedobjet = []
        
        self.image_passage = pygame.image.load("Passage.png")
        self.screen = pygame.display.set_mode((225, 225))

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
                        if element.nomdelobjet == "aiguille":
                            self.screen.blit(IMAGE_AIGUILLE, element.newtupleposition)
                        elif element.nomdelobjet == "un tube en plastique":
                            self.screen.blit(IMAGE_TUBEENPLASTIQUE, element.newtupleposition)
                        elif element.nomdelobjet == "de l'ether":  
                            self.screen.blit(IMAGE_ETHER, element.newtupleposition)
                    if (i,j) in self.malistedetuplemur:
                        self.screen.blit(IMAGE_MUR, (i*15,j*15))
                    elif (i,j) in self.malistedetuplepassage:
                        self.screen.blit(IMAGE_PASSAGE, (i*15,j*15))
                    elif i == self.gardien.ligne and j == self.gardien.colonne:
                        self.screen.blit(IMAGE_GARDIEN, (i*15,j*15))
                    elif i == self.macgyver.ligne and j == self.macgyver.colonne:
                        self.screen.blit(IMAGE_MACGYVER, (i*15,j*15))
             
                        
        

        pygame.display.flip()
        print("")
                
    def objetdanslabyrinthe(self,):
        for element in ITEMS:
            objet = Items(element, self.malistedetuplepassage)
            self.listedobjet.append(objet)
            self.malistedetuplepassage.remove(objet.tupleposition)

            #image = objet.afficherlesimages()

            #generalisation 

    



            
               

            





               
             


     

