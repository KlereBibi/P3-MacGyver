"""This module contains Macgyver's class with different methods for interacting in the labyrinth."""

import pygame
from settings.constant import FONT, COLOR, BLACK_BACKGROUND

pygame.font.init()

class MacGyver(pygame.sprite.Sprite):

    """Class of hero who move out the labyrinthe with 3 items"""

    def __init__(self, x, y):

        """constructor of the hero class

            Args:
                x (int) : horizontal position
                y (int):  vertical position

            Attributes:
                attr1 (int) : horizontal position of hero
                attr2 (int) : vertical_position of hero
                attr3 (list) : list of item
                attr4 (str) : initialization of the display size and font
                attr5 (bol) : True the game continue, False the end of the game"""

        super().__init__()
        self.horizontal_position = x
        self.vertical_position = y
        self.item_list = []
        self.myfont = pygame.font.SysFont(FONT, 18)
        self.game = True

    def next_position(self, userchoice):

        """method for applying user choice

            Args:
                userchoice : keyboard key press by user

            Returns:
                tuple of the news position  """

        if userchoice == pygame.K_RIGHT:
            return (self.horizontal_position, self.vertical_position +1)
        elif userchoice == pygame.K_DOWN:
            return (self.horizontal_position +1, self.vertical_position )
        elif userchoice == pygame.K_UP:
            return (self.horizontal_position -1, self.vertical_position )
        elif userchoice == pygame.K_LEFT:
            return (self.horizontal_position , self.vertical_position -1)

    def can_move(self, position_to_watch, list_tuple_passage,\
                list_items_labyrinth, guardian_position):

        """method allowing to know if the player can move
           Args :
                position_to_watch (tup) : position requested by use
                list_tuple_passage (list) : list with the passing tuples
                list_items_labyrinth (list) : list with the item in the labyrinthe
                guardian_position (tup) : tuple position of the guardian

            Returns:
                move (bol) : False the hero can't move, True the hero can move"""

        move = False
        if position_to_watch in list_tuple_passage or position_to_watch == guardian_position:
            move = True
        for element in list_items_labyrinth:
            if element.tuple_position == position_to_watch\
                or position_to_watch in list_tuple_passage\
                or position_to_watch == guardian_position:
                move = True
        return move

    def move_macgyver(self, userchoice, list_tuple_passage,\
                        guardian_position, list_items_labyrinth ):

        """method to move macgyver
        
           Args:
                userchoice (str) : keyboard key press by user
                list_tuple_passage (list) : list with the passing tuples
                guardian_position (tup) : tuple position of the guardian
                list_items_labyrinth (list) : list with the item in the labyrinthe"""

        position_to_watch = self.next_position(userchoice)
        if self.can_move(position_to_watch, list_tuple_passage,\
                            list_items_labyrinth, guardian_position):
            self.horizontal_position = position_to_watch[0]
            self.vertical_position = position_to_watch[1]
        if len(self.item_list) != 3:
            self.grab_the_items(list_items_labyrinth)

    def grab_the_items(self, list_items_labyrinth):

        """method to add an items on the list tuple passage to the list of items of MacGyver

            Args:
                list_items_labyrinth (list) : list with the item in the labyrinthe"""

        for element in list_items_labyrinth:
            if element.tuple_position == (self.horizontal_position, self.vertical_position):
                self.item_list.append(element)

   

    def end_of_game_test(self, guardian_position, screen, end_of_game):

        """methode test for the end of game

        Args:
            guardian_position (tuple) : tuple position of the guardian
            screen (surface) : pygame display window
            end_of_game (bol) :

        Returns:
            game (bol) : False end of the game, True the game continue """

        if (self.horizontal_position, self.vertical_position) == (guardian_position):
            if len(self.item_list) == 3:
                end = "Macgyver exits the Labyrinth"
            else:
                end = "macgyver loses"
            self.printwindow(screen, end, COLOR["blue"])
            end_of_game = False
        return end_of_game

    def items_counter(self, screen):

        """count items in macgyver's list

            Args:
                screen (surface) : pygame display window"""

        number_of_items = "Macgyver has {} item(s)".format(len(self.item_list))
        self.printwindow(screen, number_of_items, COLOR["green"])

    def printwindow(self,screen, my_text, the_color):

        """method to white the elements in the window generated by pygame

            Args:
                screen (surface) : pygame display window
                the_color (dict) : color dictionary"""

        screen.blit(BLACK_BACKGROUND, (2,230))
        textsurface = self.myfont.render(my_text, True, the_color)
        screen.blit(textsurface,(2,230))
