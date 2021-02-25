from random import choice

class Items():
    """class allowing to initialize the objects useful to Macgyver to get out of the labyrinth"""
    def __init__(self, element, lalistedepassage):
        """constructor of the class containing the position of the object, the key and the value of the object"""
        self.type_of_objet = element
        self.tuple_position = choice(lalistedepassage)
        #faire une clef générique pour objet
        self.print_value = self.type_of_objet["image"]
        self.nomdelobjet = self.type_of_objet["name"]
        self.vertical = self.tuple_position[0] 
        self.horizontal = self.tuple_position[1]
        self.new_tupleposition = (self.horizontal*15, self.vertical*15)
        
        


        

        


    