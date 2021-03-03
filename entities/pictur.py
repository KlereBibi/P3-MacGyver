from settings.constantes import MYLABYRINTH, ITEMS, WALL_PICTURE, PASSAGE_PICTURE, MACGYVER_PICTURE, GUARDIAN_PICTURE, SCREEN, PICTURE
from entities.macgyver import MacGyver
from entities.guardian import Guardian
from random import choice
from entities.item import Items
import pygame

pygame.init()
pygame.display.set_caption("Macgyver")

class Labyrinth:

    """The labyrinth class permettant de lire le fichier labyrinthe et de l'afficher avec pygame"""

    def __init__(self):

        """Constructor including tuple list of passage and walls, two dimensional array, object list and pygame viewport"""

        self.tuple_wall_list = []
        self.tuple_pass_list = []
        self.horizontal_position = 0
        self.vertical_position = 0
        self.object_list = []
        self.screen = SCREEN
        self.pictur_list = ["wall", "passage"]
        
        
    def read_file_labyrinth(self):

        """method allowing to read the referenced file in a constant with iteration"""

        my_file = open(MYLABYRINTH, "r")
        i = 0
        for line in my_file:
            j = 0
            for character in line: 
                if "m" in character:
                    self.tuple_wall_list.append((i,j))
                elif "p"  in character:
                    self.tuple_pass_list.append((i,j))
                elif "h" in character:
                    self.macgyver = MacGyver(i, j) 
                elif "g" in character:
                    self.guardian = Guardian(i, j)
                j+=1
            i += 1
        self.horizontal_position = i 
        self.vertical_position = j

    def print_labyrinth(self):

        """method allowing to display with pygame the reading of the labyrinth as well as the objects by iteration"""

        self.new_macgyver_position()
        self.print_picture()
        for i in range(self.horizontal_position):
            for j in range(self.vertical_position):
                if (i,j) in self.tuple_wall_list:
                    self.screen.blit(self.pictur_list["wall"], (j*15,i*15))
                elif (i,j) in self.tuple_pass_list:
                    self.screen.blit(PASSAGE_PICTURE, (j*15,i*15))
                elif (i,j) == self.guardian.tuple_guardian:
                    self.screen.blit(GUARDIAN_PICTURE, (j*15,i*15))
                elif i == self.macgyver.horizontal_position and j == self.macgyver.vertical_position:
                    self.screen.blit(MACGYVER_PICTURE, (j*15,i*15))
                    self.tuple_pass_list.append((self.macgyver.horizontal_position, self.macgyver.vertical_position))
                elif len(self.object_list) != 0:
                    for element in self.object_list:
                        if (i,j) == element.tuple_position:
                            self.screen.blit(element.print_value, element.new_tupleposition)             
        self.macgyver.object_counter(self.screen)
        pygame.display.flip()
        print("")

    def print_picture(self):
        for element in PICTURE:
            for each in self.pictur_list:
                if element["name"] == each:
                    self.pictur_list[element] = element["image"]
 
    def item_labyrinth(self): 

        """method initialized in the main function retrieving the item recorded in a dictionary list in the constants file and displaying them in the labyrinthe"""

        for element in ITEMS:
            the_objet = Items(element, self.tuple_pass_list)
            self.object_list.append(the_objet)
            self.tuple_pass_list.remove(the_objet.tuple_position)

    def new_macgyver_position(self):

        """method allowing the movement of the hero MacGyver within the labyrinth"""

        if len(self.object_list)>0:
            for element in self.object_list:
                if element.tuple_position == (self.macgyver.horizontal_position, self.macgyver.vertical_position):
                    self.object_list.remove(element)
                    self.tuple_pass_list.append(element.tuple_position)
        if (self.macgyver.horizontal_position, self.macgyver.vertical_position) in self.tuple_pass_list:
            self.tuple_pass_list.remove((self.macgyver.horizontal_position, self.macgyver.vertical_position))
            
