
# coding: utf-8 - spécifie l'encodage du code source de notre script

import pygame

from entities.labyrinth import Labyrinth

def main():

    """Main function of the game.
        This function initializes Pygame, initializes the maze in a variable, reads the text file of the maze, and calls the method used to create the items in the maze.
        A while mouth is created and the game only stops if the method calling move_macgyver returns a boleen False"""

    pygame.init()  
    end_of_game = True
    my_labyrinth = Labyrinth()
    my_labyrinth.read_file_labyrinth()
    my_labyrinth.item_labyrinth()
    while end_of_game:
        my_labyrinth.print_labyrinth()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                userchoice = event.key
                end_of_game = my_labyrinth.macgyver.move_macgyver(userchoice, my_labyrinth.tuple_pass_list, my_labyrinth.guardian.tuple_guardian, my_labyrinth.object_list, end_of_game, my_labyrinth.screen)        
                my_labyrinth.print_labyrinth()
    
if __name__ == '__main__':
    main()

