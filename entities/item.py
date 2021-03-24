"""Module with the items class to generate in the labyrinth"""

from random import choice

class Items():

    """class allowing to initialize the item useful to Macgyver to get out of the labyrinth"""

    def __init__(self, element, passage_list):

        """Constructor of the class

            Args:
                element (dict) : the first parametre
                passage_list (list) : the second parametre

            Attributs:
                attr1 (dict) : item dictionary
                attr2 (tup) : tuple chooses from the pass list
                attr3 (str) : the value of the element key
                attr4 (int) : horizontal position
                attr5 (int) : vertical position
                attr6 (tup) : position to display with pygame"""

        self.type_of_items = element
        self.tuple_position = choice(passage_list)
        self.print_value = self.type_of_items["image"]
        self.vertical = self.tuple_position[0]
        self.horizontal = self.tuple_position[1]
        self.new_tupleposition = (self.horizontal*15, self.vertical*15)
