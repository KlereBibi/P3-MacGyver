
# coding: utf-8 - spécifie l'encodage du code source de notre script


from fonctions.labyrinthe import Labyrinthe
import pygame
pygame.init()

#générer la fenêtre


def main():
    

    sortiedulabyrinthe = True
    monlabyrinthe = Labyrinthe()
    monlabyrinthe.readlab()
    monlabyrinthe.objetdanslabyrinthe()
    while sortiedulabyrinthe:
        monlabyrinthe.printlab()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                userchoice = event.key
                sortiedulabyrinthe = monlabyrinthe.macgyver.movemacgyver(userchoice, monlabyrinthe.malistedetuplepassage, monlabyrinthe.gardien.tuplegardien, monlabyrinthe.listedobjet, sortiedulabyrinthe)    
        pygame.display.flip()    
        monlabyrinthe.printlab()   

if __name__ == '__main__':
    main()

