"""this module contains the labyrinth class to display with pygame"""

import pygame
from settings.constant import MYLABYRINTH, ITEMS, SCREEN, PICTURE
from entities.macgyver import MacGyver
from entities.guardian import Guardian
from entities.item import Items

pygame.init()
pygame.display.set_caption("Macgyver")

class Labyrinth:

    """The labyrinth class allowing to create, display and update the labyrinth"""

    def __init__(self):

        """Constructor of class

            Attributes:
                attr1 (list) : list tuple of wall
                attr2 (list) : list tuple of passage
                attr3 (int) : horizontal position
                attr4 (int) : vertical position
                attr5 (list) : list item
                attr6 (surface) : pygame display window """

        self.tuple_wall_list = []
        self.tuple_pass_list = []
        self.max_horizontal_position = 0
        self.max_vertical_position = 0
        self.item_list = []
        self.screen = SCREEN

    def read_file_labyrinth(self):

        """method allowing to read the referenced file in a constant with iteration"""

        my_file = open(MYLABYRINTH, "r")
        i = 0
        for line in my_file:
            j = 0
            for character in line:
                if "m" in character:
                    self.tuple_wall_list.append((i,j))
                elif "p" in character:
                    self.tuple_pass_list.append((i,j))
                elif "h" in character:
                    self.macgyver = MacGyver(i, j)
                elif "g" in character:
                    self.guardian = Guardian(i, j)
                j+=1
            i += 1
        self.max_horizontal_position = i
        self.max_vertical_position = j

    def print_labyrinth(self):

        """maze display method with pygame"""

        self.new_macgyver_position()
        for i in range(self.max_horizontal_position):
            for j in range(self.max_vertical_position):
                if (i,j) in self.tuple_wall_list:
                    self.screen.blit(PICTURE["wall"] , (j*15,i*15))
                elif (i,j) in self.tuple_pass_list:
                    self.screen.blit(PICTURE["passage"], (j*15,i*15))
                elif (i,j) == self.guardian.tuple_guardian:
                    self.screen.blit(PICTURE["guardian"], (j*15,i*15))
                elif i == self.macgyver.horizontal_position\
                        and j == self.macgyver.vertical_position:
                    self.screen.blit(PICTURE["macgyver"], (j*15,i*15))
                    self.tuple_pass_list.append\
                        ((self.macgyver.horizontal_position, self.macgyver.vertical_position))
                elif len(self.item_list) != 0:
                    for element in self.item_list:
                        if (i,j) == element.tuple_position:
                            self.screen.blit(element.print_value, element.new_tupleposition)
        pygame.display.flip()
        print("")

    def item_labyrinth(self):

        """method generating the items"""

        for element in ITEMS:
            the_objet = Items(element, self.tuple_pass_list)
            self.item_list.append(the_objet)
            self.tuple_pass_list.remove(the_objet.tuple_position)

    def new_macgyver_position(self):

        """method allowing the movement of the hero MacGyver within the labyrinth"""

        if len(self.item_list)>0:
            for element in self.item_list:
                if element.tuple_position ==\
                    (self.macgyver.horizontal_position, self.macgyver.vertical_position):
                    self.item_list.remove(element)
                    self.tuple_pass_list.append(element.tuple_position)
        if (self.macgyver.horizontal_position, self.macgyver.vertical_position) in\
                 self.tuple_pass_list:
            self.tuple_pass_list.remove\
                ((self.macgyver.horizontal_position, self.macgyver.vertical_position))
