
# coding: utf-8 - spécifie l'encodage du code source de notre script
import pygame


from fonctions.labyrinthe import Labyrinthe


def main():
    pygame.init()
    sortiedulabyrinthe = True
    monlabyrinthe = Labyrinthe()
    monlabyrinthe.readlab()
    monlabyrinthe.objetdanslabyrinthe()
    while sortiedulabyrinthe:
        monlabyrinthe.printlab()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                userchoice = event.key
                sortiedulabyrinthe = monlabyrinthe.macgyver.movemacgyver(userchoice, monlabyrinthe.malistedetuplepassage, monlabyrinthe.gardien.tuplegardien, monlabyrinthe.listedobjet, sortiedulabyrinthe, monlabyrinthe.screen)        
        monlabyrinthe.printlab()
        pygame.display.flip()
        if not sortiedulabyrinthe:
            input("")
if __name__ == '__main__':
    main()

