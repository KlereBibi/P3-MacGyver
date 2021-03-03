import pygame
from settings.constantes import MY_FONT, COLOR, BLACK_BACKGROUND, PICTURE

pygame.font.init()

class MacGyver(pygame.sprite.Sprite):

    """Class of hero who move out the labyrinthe with 3 items"""

    def __init__(self, x, y):

        """constructor of the hero class including horizontal and vertical position, item list, font, and a boleen
            
            The constructor takes as argument:
            - a horizontal x position
            - a vertical y position
            present in a two-dimensional array """

        super().__init__()
        self.horizontal_position = x
        self.vertical_position = y 
        self.object_list = []
        #self.myfont = pygame.font.SysFont(FONT, 18)
        self.game = True


    def next_position(self, userchoice):

        """method for applying user choice
            The method takes as argument:
            - the "userchoice" variable containing the key operated by the user on the keyboard
            The new position of the hero will be returned according to the keyboard key activate """

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

           The method takes as arguments:
            - the variable containing the new displacement coordinates of macgyver defined by the next_position method
            - the tuple pass list: allows you to check if the variable corresponds to one of the tuples
            - the list of items: allows you to check if the variable corresponds to the position of an item in the labyrinth
            - the position in the form of a tuple of the guardian: allows you to check if the variable corresponds to the
            
            The method will revert to a True boleen if Macgyver can move, otherwise it will remain False and no movement will take place"""

        move = False
        if position_to_watch in list_tuple_passage or position_to_watch == guardian_position:
            move = True
        for element in list_items_labyrinth:
            if element.tuple_position == position_to_watch or position_to_watch in list_tuple_passage or position_to_watch == guardian_position:
                move = True 
        return move

    def grab_the_object(self, position_to_watch, list_items_labyrinth):

        """method allowing to add an items on the list tuple passage to the list of items of MacGyver
            
            The method takes as arguments:
            - the variable containing the new displacement coordinates of macgyver defined by the next_position method
            _ the list of items: allows you to check if the variable corresponds to the position of an item in the labyrinth"""

        for element in list_items_labyrinth:
            if element.tuple_position == position_to_watch:
                self.object_list.append(element)

    def move_macgyver(self, userchoice, list_tuple_passage, guardian_position, list_items_labyrinth, boleen, screen):

        """method using the other methods to check if movement is possible, give MacGyver its new position, test the end of the game and use the method to grab objects
            
            The method takes as arguments:
            - the variable "userchoice" containing the choice of the user to use in the method allowing to validate the displacement
            - the list of passing tuple used in several different methods: to validate the move, grab the items
            - the guardian position tuple used in the method used to validate the move and to know if it is the end of the game
            - the list of items present in the labyrinth use to know the position of macgyver and to catch the objects 
            - the boleen of the while loop in the main function
            - access to the maze display in order to register the items counter
            The method returns a boleen by the method testing the end of the game. If Macgyver's position is the same as the goalkeeper, then a False boleen will be returned. """
            
        position_to_watch = self.next_position(userchoice)
        if self.can_move(position_to_watch, list_tuple_passage, list_items_labyrinth, guardian_position):
            self.horizontal_position = position_to_watch[0]
            self.vertical_position = position_to_watch[1]
            test = self.end_of_game_test(guardian_position, screen)
            if len(self.object_list) != 3:
                self.grab_the_object(position_to_watch, list_items_labyrinth)
            if not test:
                boleen = False 
        return boleen
        

    def end_of_game_test(self, guardian_position, screen):

        """method using a condition to know if the position of MacGyver was the same as that of the guardian position, and if Macgyver had indeed the 3 objects to exit 
        
        The method takes as arguments:
        - the guardian position tuple: if the position of the guardian is the same as that of macgyver then the game ends 
        - the variable containing the pygame display window allowing you to enter whether Macgyver has won or lost
        The method returns a boleen False if the position of macgyver is the same as that of the guardian, and True if it is not"""
        
        if (self.horizontal_position, self.vertical_position) == (guardian_position):
            if len(self.object_list) == 3:
                end = "Macgyver exits the Labyrinth"
            else:
                end = "macgyver loses"
            blue = COLOR[2]
            self.printwindow(screen, end, blue["color"])
            self.game = False
        return self.game
        
    def object_counter(self, screen):

        """method using the constructor's items list to white the number of objects in its possession
            The method takes as argument:
            - the variable containing the pygame display window used to display the items counter"""
        
        if self.game: 
            number_of_objects = "Macgyver has {} item(s)".format(len(self.object_list))
            green = COLOR[0]            
            self.printwindow(screen, number_of_objects, green["color"])
        
    def printwindow(self,screen, my_text, the_colour):

        """method to white the elements in the window generated by pygame

            The method takes as argument:
            - text displayed
            - the color of the text to display as a constant"""

        screen.blit(BLACK_BACKGROUND, (2,230))
        textsurface = MY_FONT.render(my_text, True, the_colour)
        screen.blit(textsurface,(2,230))
        
