import pygame

MONLABYRINTHE = "fonctions/labyrinthe.txt" #chemin que je lui donne donc /
ITEMS = [{"name" : "aiguille", "image" : pygame.image.load("images/aiguille.PNG")}, {"name" : "un tube en plastique", "image" : pygame.image.load("images/tube_plastique.PNG")}, {"name" : "de l'ether", "image" : pygame.image.load("images/ether.PNG")}]
IMAGE_MUR = pygame.image.load("images/mur.png")
IMAGE_PASSAGE = pygame.image.load("images/Passage.png")
IMAGE_MACGYVER = pygame.image.load("images/MacGyver.png")
IMAGE_GARDIEN = pygame.image.load("images/Gardien.PNG")
 #mettre dans le dictionnaire
VERT = pygame.Color(0, 255, 0)
POLICE = "arial"
NOIR = pygame.Color(0, 0 , 0)
FONDNOIR = pygame.image.load("images/fondnoir.PNG")
BLEU = pygame.Color(0,0,255)

# tout mettre en anglias
# écrire les docstring 
