
# coding: utf-8 - spécifie l'encodage du code source de notre script

from fonctions.labyrinthe import Labyrinthe
import pygame
pygame.init()

#générer la fenêtre


def main():
    
    monlabyrinthe = Labyrinthe()
    monlabyrinthe.readlab()
    monlabyrinthe.objetdanslabyrinthe()
    monlabyrinthe.printlab()
    sortiedulabyrinthe = False
    
    while not sortiedulabyrinthe :
        #userchoice = input("Merci de sélectionner u pour monter, d pour descendre, l pour gauche et r pour droite:  ") 
        
        userchoice = pygame.event.get()
        sortiedulabyrinthe = monlabyrinthe.macgyver.movemacgyver(userchoice, monlabyrinthe.malistedetuplepassage, monlabyrinthe.gardien.tuplegardien, monlabyrinthe.listedobjet, sortiedulabyrinthe, monlabyrinthe.gardien.listedobjet)
        if sortiedulabyrinthe:
            continue
        monlabyrinthe.printlab()
        monlabyrinthe.macgyver.compteurdobjet()
 

if __name__ == '__main__':
    main()

