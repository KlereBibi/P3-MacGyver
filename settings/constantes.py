import pygame


MYLABYRINTH = "entities/labyrinth.txt" 
ITEMS = [{"name" : "NEEDLE", "image" : pygame.image.load("sprites/needle.PNG")}, {"name" : "PLASTIC TUBE", "image" : pygame.image.load("sprites/plastic_tube.PNG")}, {"name" : "ETHER", "image" : pygame.image.load("sprites/ether.PNG")}]
PICTURE = [{ "name" : "WALL", "image" : pygame.image.load("sprites/wall.png")}, {"name" : "PASSAGE", "image" : pygame.image.load("sprites/passage.png")}, {"name" : "GUARDIAN", "image" : pygame.image.load("sprites/guardian.PNG")}, {"name" : "MACGYVER", "image" : pygame.image.load("sprites/macgyver.png")}]
COLOR = [{"name" : "GREEN_COLOR", "color" : pygame.Color(0, 255, 0)}, {"name" : "BLACK_COLOR", "color" : pygame.Color(0, 0 , 0)}, {"name" : "BLUE_COLOR", "color" : pygame.Color(0,0,255)}]
MY_FONT = pygame.font.SysFont("arial", 18)
BLACK_BACKGROUND = pygame.image.load("sprites/black_background.PNG")
SCREEN = pygame.display.set_mode((225, 255))




