import pygame

MYLABYRINTH = "entities/labyrinth.txt" 
ITEMS = [{"name" : "needle", "image" : pygame.image.load("sprites/needle.PNG")}, {"name" : "plastic tube", "image" : pygame.image.load("sprites/plastic_tube.PNG")}, {"name" : "ether", "image" : pygame.image.load("sprites/ether.PNG")}]
PICTURE = [{ "name" : "WALL", "image" : pygame.image.load("sprites/wall.png")}, {"name" : "PASSAGE", "image" : pygame.image.load("sprites/passage.png")}, {"name" : "GUARDIAN", "image" : pygame.image.load("sprites/guardian.PNG")}, {"name" : "MACGYVER", "image" : pygame.image.load("sprites/macgyver.png")}]
GREEN_COLOR = pygame.Color(0, 255, 0)
FONT = "arial"
BLACK_COLOR = pygame.Color(0, 0 , 0)
BLACK_BACKGROUND = pygame.image.load("sprites/black_background.PNG")
BLUE_COLOR = pygame.Color(0,0,255)
SCREEN = pygame.display.set_mode((225, 255))




