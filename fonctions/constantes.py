import pygame

MONLABYRINTHE = "fonctions/labyrinthe.txt" #chemin que je lui donne donc /
ITEMS = [{"name" : "aiguille", "image" : "a"}, {"name" : "un tube en plastique", "image" : "t"}, {"name" : "de l'ether", "image" : "e"}]
IMAGE_MUR = pygame.image.load("mur.png")
IMAGE_PASSAGE = pygame.image.load("Passage.png")
IMAGE_MACGYVER = pygame.image.load("MacGyver.png")
IMAGE_GARDIEN = pygame.image.load("Gardien.PNG")
IMAGE_ETHER = pygame.image.load("ether.PNG")
IMAGE_AIGUILLE = pygame.image.load("aiguille.PNG")
IMAGE_TUBEENPLASTIQUE = pygame.image.load("tube_plastique.PNG")
