#!/usr/bin/python3

"""
a class Square that inherits from Rectangle
Instantiation with size: def __init__(self, size):
size must be private.
size must be a positive integer,
validated by integer_validator
the area() method must be implemented
"""

# Import function
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a square class
    """
    def __init__(self, size):
        """
        initializes the square class
        """
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """
        string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
