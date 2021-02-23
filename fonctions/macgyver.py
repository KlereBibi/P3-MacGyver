import pygame
from fonctions.constantes import VERT
from fonctions.constantes import POLICE
from fonctions.constantes import NOIR
from fonctions.constantes import FONDNOIR
from fonctions.constantes import BLEU

pygame.font.init()

class MacGyver(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.ligne = x
        self.colonne = y 
        self.tuplemacgyver = (self.ligne, self.colonne)
        self.listedobjet = []
        self.myfont = pygame.font.SysFont(POLICE, 18)
        self.game = True


    def lecturedelinput(self, event):

        if event == pygame.K_RIGHT:
            return (self.ligne, self.colonne +1)
        if event == pygame.K_DOWN:
            return (self.ligne +1, self.colonne )
        elif event == pygame.K_UP:
            return (self.ligne -1, self.colonne )
        elif event == pygame.K_LEFT:
            return (self.ligne , self.colonne -1)

    
    def chekmove(self, variable, passage, listedobjetlabyrinthe, gardien):
        move = False
        if variable in passage or variable == gardien:
            move = True
        for element in listedobjetlabyrinthe:
            if element.tupleposition == variable or variable in passage or variable == gardien:
                move = True 
        return move

    def attrapelobjet(self, variable, listedobjetlabyrinthe):
        for element in listedobjetlabyrinthe:
            if element.tupleposition == variable:
                self.listedobjet.append(element)

    def movemacgyver(self, event, passage, gardien, listedobjetlabyrinthe, boleen, screen):
  
        positionaregarder = self.lecturedelinput(event)
        if self.chekmove( positionaregarder, passage, listedobjetlabyrinthe, gardien):
            self.ligne = positionaregarder[0]
            self.colonne = positionaregarder[1] 
            test = self.testcontinue(gardien, passage, screen)
            if len(self.listedobjet) != 3:
                objet = self.attrapelobjet(positionaregarder, listedobjetlabyrinthe)
            if not test:
                boleen = False 
        return boleen

    def testcontinue(self, gardien, passage, screen):
        
        if (self.ligne, self.colonne) == (gardien):
            if len(self.listedobjet) == 3:
                fin = "Macgyver sort du Labyrinthe"
            else:
                fin = "Macgyver perd"
            self.game = False
            self.printwindow(screen, fin, BLEU)
        return self.game
        
    def compteurdobjet(self, screen):
        
        if self.game: 
            nbrobjet = "MacGyver a {} objet(s)".format(len(self.listedobjet))            
            self.printwindow(screen, nbrobjet, VERT)
        
    def printwindow(self,screen, jaffiche, couleur):
        screen.blit(FONDNOIR,(2,230))
        textsurface = self.myfont.render(jaffiche, True, couleur)
        screen.blit(textsurface,(2,230))
       
        