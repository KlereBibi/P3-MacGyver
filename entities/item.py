from random import choice

class Items():

    """class allowing to initialize the item useful to Macgyver to get out of the labyrinth"""

    def __init__(self, element, passage_list):

        """Constructor of the class containing the position of the items, the key and the value of the items.
            
            The constructor takes as argument:
            - the item chooses from the list to save the elements of the item's dictionary in a variable
            - the passing tuple list to randomly find the item's position with the random"""
            
        self.type_of_items = element
        self.tuple_position = choice(passage_list)
        self.print_value = self.type_of_items["image"]
        self.name_of_item = self.type_of_items["name"]
        self.vertical = self.tuple_position[0] 
        self.horizontal = self.tuple_position[1]
        self.new_tupleposition = (self.horizontal*15, self.vertical*15)
        


        

        


    