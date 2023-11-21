#!/usr/bin/python3

"""a class that defines a square"""


class Square:
    """defines a class"""
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
