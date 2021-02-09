
# coding: utf-8 - spécifie l'encodage du code source de notre script

from fonctions.labyrinthe import Labyrinthe
import pygame
pygame.init()

#générer la fenêtre


def main():
    
    
    #monlabyrinthe.objetdanslabyrinthe()

    continuer = True
    monlabyrinthe = Labyrinthe()
    monlabyrinthe.readlab()
    while continuer:
        pygame.display.flip()
        monlabyrinthe.printlab()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    (monlabyrinthe.macgyver.ligne + 15, monlabyrinthe.macgyver.colonne)
                elif event.key == pygame.K_RIGHT:
                    (monlabyrinthe.macgyver.ligne, monlabyrinthe.macgyver.colonne +15)
                elif event.key == pygame.K_LEFT:
                    (monlabyrinthe.macgyver.ligne, monlabyrinthe.macgyver.colonne -15)
                elif event.key == pygame.K_UP:
                    (monlabyrinthe.macgyver.ligne -15, monlabyrinthe.macgyver.colonne)
        pygame.display.flip()      
       


        
                

"""   
    sortiedulabyrinthe = False

    while not sortiedulabyrinthe :
        #userchoice = input("Merci de sélectionner u pour monter, d pour descendre, l pour gauche et r pour droite:  ") 
        monlabyrinthe.printlab()
        userchoice = pygame.event.get()
        sortiedulabyrinthe = monlabyrinthe.macgyver.movemacgyver(userchoice, monlabyrinthe.malistedetuplepassage, monlabyrinthe.gardien.tuplegardien, monlabyrinthe.listedobjet, sortiedulabyrinthe, monlabyrinthe.gardien.listedobjet)
        if sortiedulabyrinthe:
            continue
        monlabyrinthe.printlab()
        monlabyrinthe.macgyver.compteurdobjet()
"""

if __name__ == '__main__':
    main()

