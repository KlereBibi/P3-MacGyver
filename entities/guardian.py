"""This module contains the guard's class to start his position."""

class Guardian:

    """Class guardian """

    def __init__(self, x, y):

        """Constructor of the class

        Args:
            x (int) : horizontal position
            y (int) : verticale position

        Attributs:
            tuple_guardian (tuple) : position of guardian"""

        self.tuple_guardian = (x,y)
