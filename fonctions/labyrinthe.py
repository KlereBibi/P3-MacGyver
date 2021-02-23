from fonctions.constantes import MONLABYRINTHE
from fonctions.constantes import ITEMS
from fonctions.constantes import IMAGE_MUR
from fonctions.constantes import IMAGE_PASSAGE
from fonctions.constantes import IMAGE_MACGYVER
from fonctions.constantes import IMAGE_GARDIEN
from fonctions.macgyver import MacGyver
from fonctions.gardien import Gardien
from random import choice
from fonctions.objets import Items
import pygame
pygame.init()
pygame.display.set_caption("Macgyver")

class Labyrinthe:

    def __init__(self):
        self.malistedetuplemur = []
        self.malistedetuplepassage = []
        self.horizontal = 0
        self.vertical = 0
        self.listedobjet = []
        self.screen = pygame.display.set_mode((225, 255))
        
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
                    self.macgyver = MacGyver(i, j) 
                elif "g" in character:
                    self.gardien = Gardien(i, j)
                j+=1
            i += 1
        self.horizontal = i 
        self.vertical = j

    def printlab(self): 
        self.deplacementheros()
        for i in range(self.horizontal):
            for j in range(self.vertical):
                if (i,j) in self.malistedetuplemur:
                    self.screen.blit(IMAGE_MUR, (j*15,i*15))
                elif (i,j) in self.malistedetuplepassage:
                    self.screen.blit(IMAGE_PASSAGE, (j*15,i*15))
                elif i == self.gardien.ligne and j == self.gardien.colonne:
                    self.screen.blit(IMAGE_GARDIEN, (j*15,i*15))
                elif i == self.macgyver.ligne and j == self.macgyver.colonne:
                    self.screen.blit(IMAGE_MACGYVER, (j*15,i*15))
                    self.malistedetuplepassage.append((self.macgyver.ligne, self.macgyver.colonne))
                elif len(self.listedobjet) != 0:
                    for element in self.listedobjet:
                        if (i,j) == element.tupleposition:
                            self.screen.blit(element.printvaleur, element.newtupleposition)             
        self.macgyver.compteurdobjet(self.screen)
        pygame.display.flip()
        print("")

    def objetdanslabyrinthe(self): # quand macgyver se déplace il attrape l'objet - se déplace sur l'objet
        for element in ITEMS:
            objet = Items(element, self.malistedetuplepassage)
            self.listedobjet.append(objet)
            self.malistedetuplepassage.remove(objet.tupleposition)

    def deplacementheros(self):
        if len(self.listedobjet)>0:
            for element in self.listedobjet:
                if element.tupleposition == (self.macgyver.ligne, self.macgyver.colonne):
                    self.listedobjet.remove(element)
                    self.malistedetuplepassage.append(element.tupleposition)
        if (self.macgyver.ligne, self.macgyver.colonne) in self.malistedetuplepassage:
            self.malistedetuplepassage.remove((self.macgyver.ligne, self.macgyver.colonne))
