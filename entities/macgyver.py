import pygame
from settings.constantes import FONT, COLOR, BLACK_BACKGROUND, PICTURE

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
                userchoice (str): the alone parametre
            
            Returns:
                tuple of the news position  """

        if userchoice == pygame.K_RIGHT:
            return (self.horizontal_position, self.vertical_position +1)
        if userchoice == pygame.K_DOWN:
            return (self.horizontal_position +1, self.vertical_position )
        elif userchoice == pygame.K_UP:
            return (self.horizontal_position -1, self.vertical_position )
        elif userchoice == pygame.K_LEFT:
            return (self.horizontal_position , self.vertical_position -1)

    
    def can_move(self, position_to_watch, list_tuple_passage, list_items_labyrinth, guardian_position):

        """method allowing to know if the player can move

           Args :
                position_to_watch (tup) : the first parametre
                list_tuple_passage (list) : the second parametre
                list_items_labyrinth (list) : the third parametre
                guardian_position (tup) : the fourth parametre

            Returns:
                move (bol) : False the hero can't move, True the hero can move"""

        move = False
        if position_to_watch in list_tuple_passage or position_to_watch == guardian_position:
            move = True
        for element in list_items_labyrinth:
            if element.tuple_position == position_to_watch or position_to_watch in list_tuple_passage or position_to_watch == guardian_position:
                move = True 
        return move

    def grab_the_object(self, position_to_watch, list_items_labyrinth):

        """method allowing to add an items on the list tuple passage to the list of items of MacGyver
            
            Args:
                position_to_watch (tuple) : the first parametre
                list_items_labyrinth (list) : the second parametre"""

        for element in list_items_labyrinth:
            if element.tuple_position == position_to_watch:
                self.item_list.append(element)

    def move_macgyver(self, userchoice, list_tuple_passage, guardian_position, list_items_labyrinth, boleen, screen):

        """method using the other methods to check if movement is possible, give MacGyver its new position, test the end of the game and use the method to grab objects
            
           Args:
                userchoice (str) : the first parametre
                list_tuple_passage (list) : the second parametre
                guardian_position (tup) : the third parametre
                list_items_labyrinth (list) : the fourth parametre
                boleen (bol) : the fifth parametre
                screen (surface) : the sixth parametre
            
            Returns:
                boleen : False end of the game, True the game continue """
            
        position_to_watch = self.next_position(userchoice)
        if self.can_move(position_to_watch, list_tuple_passage, list_items_labyrinth, guardian_position):
            self.horizontal_position = position_to_watch[0]
            self.vertical_position = position_to_watch[1]
            test = self.end_of_game_test(guardian_position, screen)
            if len(self.item_list) != 3:
                self.grab_the_object(position_to_watch, list_items_labyrinth)
            if not test:
                boleen = False 
        return boleen
        

    def end_of_game_test(self, guardian_position, screen):

        """method using a condition to know if the position of MacGyver was the same as that of the guardian position, and if Macgyver had indeed the 3 objects to exit 
        
        Args:
            guardian_position (tuple) : the first parametre
            screen (surface) : the sixth parametre
        
        Returns:
            game (bol) : False end of the game, True the game continue """

        if (self.horizontal_position, self.vertical_position) == (guardian_position):
            if len(self.item_list) == 3:
                end = "Macgyver exits the Labyrinth"
            else:
                end = "macgyver loses"
            self.printwindow(screen, end, COLOR["blue"])
            self.game = False
        return self.game
        
    def object_counter(self, screen):

        """method using the constructor's items list to white the number of objects in its possession
            
            Args:
                screen (surface) : the alone parametre"""
        
        if self.game: 
            number_of_objects = "Macgyver has {} item(s)".format(len(self.item_list))          
            self.printwindow(screen, number_of_objects, COLOR["green"])
        
    def printwindow(self,screen, my_text, the_color):

        """method to white the elements in the window generated by pygame

            Args:
                screen (surface) : the first parametre
                the_color (dict) : the second parametre"""

        screen.blit(BLACK_BACKGROUND, (2,230))
        textsurface = self.myfont.render(my_text, True, the_color)
        screen.blit(textsurface,(2,230))
        
