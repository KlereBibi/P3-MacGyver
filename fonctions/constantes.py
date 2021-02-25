import pygame

MYLABYRINTH = "fonctions/labyrinth.txt" 
ITEMS = [{"name" : "aiguille", "image" : pygame.image.load("images/aiguille.PNG")}, {"name" : "un tube en plastique", "image" : pygame.image.load("images/tube_plastique.PNG")}, {"name" : "de l'ether", "image" : pygame.image.load("images/ether.PNG")}]
WALL_PICTURE = pygame.image.load("images/mur.png")
PASSAGE_PICTURE = pygame.image.load("images/Passage.png")
MACGYVER_PICTURE = pygame.image.load("images/MacGyver.png")
GUARDIAN_PICTURE = pygame.image.load("images/Gardien.PNG")
GREEN_COLOR = pygame.Color(0, 255, 0)
FONT = "arial"
BLACK_COLOR = pygame.Color(0, 0 , 0)
BLACK_BACKGROUND = pygame.image.load("images/fondnoir.PNG")
BLUE_COLOR = pygame.Color(0,0,255)


