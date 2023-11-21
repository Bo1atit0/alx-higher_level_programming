#!/usr/bin/python3

"""
Creates a class that defines a square.
Private instance attribute: size
"""


class Square:
    """
    defines a class with attribute size=0
    checks if size is of type int and
    if size < 0
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
