#!/usr/bin/python3

"""
Creates a class that defines a square with
private instance attribute: size
"""


class Square:
    """
    Defines a class with attribute size=0.
    checks for certain conditions.
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
