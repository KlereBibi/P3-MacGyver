
# coding: utf-8 - spécifie l'encodage du code source de notre script

import pygame

from fonctions.labyrinth import Labyrinth

def main():
    """main function of the game"""
    pygame.init() 
    end_of_game = True
    my_labyrinth = Labyrinth()
    my_labyrinth.read_file_labyrinth()
    my_labyrinth.object_labyrinth()
    while end_of_game:
        my_labyrinth.print_labyrinth()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                userchoice = event.key
                end_of_game = my_labyrinth.macgyver.move_macgyver(userchoice, my_labyrinth.tuple_pass_list, my_labyrinth.guardian.tuple_guardian, my_labyrinth.object_list, end_of_game, my_labyrinth.screen)        
                my_labyrinth.print_labyrinth()
    
if __name__ == '__main__':
    main()

