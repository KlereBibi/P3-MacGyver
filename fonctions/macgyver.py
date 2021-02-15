import pygame

pygame.font.init()



class MacGyver(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.ligne = x
        self.colonne = y 
        self.tuplemacgyver = (self.ligne, self.colonne)
        self.listedobjet = []
        self.image = pygame.image.load("MacGyver.png")
        self.myfont = pygame.font.SysFont("Times New Roman", 18)


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
        
        for element in listedobjetlabyrinthe:
            if element.tupleposition == variable:
                objettrouver = element
                self.attrapelobjet(passage, objettrouver, listedobjetlabyrinthe)  
        if variable in passage or variable == gardien:
            move = True
        
        return move

    def movemacgyver(self, event, passage, gardien, listedobjetlabyrinthe, boleen):
  
        
        positionaregarder = self.lecturedelinput(event)
        if self.chekmove( positionaregarder, passage, listedobjetlabyrinthe, gardien):
            passage.append((self.ligne, self.colonne))
            self.ligne = positionaregarder[0]
            self.colonne = positionaregarder[1] 
            test = self.testcontinue(gardien, passage)
            if test:
                passage.remove((self.ligne, self.colonne))
            else:
                boleen = False
        else:
            print("merci de recommencer")
   
        return boleen

    def testcontinue(self, gardien, passage):
        game = True
        if (self.ligne, self.colonne) == (gardien):
            if len(self.listedobjet) == 3:
                game = False    
        return game
        
    def attrapelobjet(self, passage, objettrouver, listedobjetlabyrinthe):
        passage.append(objettrouver.tupleposition)
        self.listedobjet.append(objettrouver)
    
    def compteurdobjet(self, screen):

        while len(self.listedobjet) == 0:
            textsurface = self.myfont.render("Macgyver a 0 objet", True, pygame.Color(0, 255, 0))
        
        while len(self.listedobjet) == 1:
            textsurface = self.myfont.render("Macgyver a 1 objet", True, pygame.Color(0, 255, 0))
            
        screen.blit(textsurface,(2,230))
             
"""elif  len(self.listedobjet) == 2:
    textsurface = self.myfont.render("Macgyver a 2 objets.", True, pygame.Color(0, 255, 0))
    
elif len(self.listedobjet) == 3:
    textsurface = self.myfont.render("Macgyver a 3 objets.", True, pygame.Color(0, 255, 0)) """
        
        
        
        