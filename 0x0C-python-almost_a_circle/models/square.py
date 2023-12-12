#!/usr/bin/python3

from models.rectangle import Rectangle

"""
A square class
Inherits from Rectangle class
"""


class Square(Rectangle):
    """
    class Square that inherits from Rectangle class
    Class constructor:
    def __init__(self, size, x=0, y=0, id=None):
    Call the super class with id, x, y, width and height
    this super call will use the logic of the __init__ of the Rectangle class.
    The width and height must be assigned to the value of size
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize a square instance using
        logic from rectangle class
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        return size value
        """
        return self.width

    @size.setter
    def size(self, new_size):
        """
        set size to a new value
        """
        self.width = new_size
        self.height = new_size

    def __str__(self):
        """
        print string representation of square instance
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
