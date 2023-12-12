#!/usr/bin/python3

from models.rectangle import Rectangle

"""
A square class
Inherits from Rectangle class
"""


class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
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
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
