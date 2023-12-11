#!/usr/bin/python3

"""
Create a class that defines a square
with private attribute: size
"""


class Square:
    """
    Initialize the attribute size
    and raises errors if conditions are not met
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Returns area of square
        """
        return (self.__size * self.__size)
