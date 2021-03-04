import pygame


MYLABYRINTH = "entities/labyrinth.txt" 
ITEMS = [{"name" : "NEEDLE", "image" : pygame.image.load("sprites/needle.PNG")}, {"name" : "PLASTIC TUBE", "image" : pygame.image.load("sprites/plastic_tube.PNG")}, {"name" : "ETHER", "image" : pygame.image.load("sprites/ether.PNG")}]
PICTURE = {"wall" : pygame.image.load("sprites/wall.png"), "passage" : pygame.image.load("sprites/passage.png"), "guardian" : pygame.image.load("sprites/guardian.PNG"), "macgyver" : pygame.image.load("sprites/macgyver.png")}
COLOR = {"green" : pygame.Color(0, 255, 0), "blue" : pygame.Color(0,0,255) }
FONT = "arial"
BLACK_BACKGROUND = pygame.image.load("sprites/black_background.PNG")
SCREEN = pygame.display.set_mode((225, 255))




