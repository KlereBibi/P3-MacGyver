

# coding: utf-8 - spécifie l'encodage du code source de notre script

"""This module contains the main function of the game"""

import pygame
from entities.labyrinth import Labyrinth

def main():

    """Main function of the game. """

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
                my_labyrinth.macgyver.move_macgyver(userchoice, my_labyrinth.tuple_pass_list, my_labyrinth.guardian.tuple_guardian, my_labyrinth.item_list)
                end_of_game = my_labyrinth.macgyver.end_of_game_test(my_labyrinth.guardian.tuple_guardian, my_labyrinth.screen, end_of_game)       
                if end_of_game:
                    my_labyrinth.macgyver.items_counter(my_labyrinth.screen)
                my_labyrinth.print_labyrinth()
                
if __name__ == '__main__':
    main()

