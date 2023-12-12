#!/usr/bin/python3

"""
A square class
Inherits from Rectangle class
"""

from models.rectangle import Rectangle


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

    def update(self, *args, **kwargs):
        """
        updates the attributes of the square class
        using *args and **kwargs
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs:
                keys = {"id", "size", "x", "y"}
                for key, value in kwargs.items():
                    if key in keys:
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation
        of a Square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
