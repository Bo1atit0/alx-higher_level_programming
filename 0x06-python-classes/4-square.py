#!/usr/bin/python3

"""
Create  a class Square that defines a square
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it
check for conditions before setting values
Public instance method: def area(self): that returns the
current square area
"""


class Square:
    def __init__(self, size=0):
        """
        Instantiation with optional size: def __init__(self, size=0)
        """

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns: area
        """
        return (self.__size ** 2)
