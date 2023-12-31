#!/usr/bin/python3
"""
 a class Rectangle that defines a rectangle
private instance attribute: width, height
Raises: errors if conditions are not met
"""


class Rectangle:
    """
    instantiating variales width and height
    Parameters:
                width
                height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        # get width
        return self.__width

    @width.setter
    def width(self, value):
        # make sure width is an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")

        # width must be >= 0
        if value < 0:
            raise ValueError("width must be >= 0")
        # set width
        self.__width = value

    @property
    def height(self):
        # get height
        return self.__height

    @height.setter
    def height(self, value):
        # height must be an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")

        # height >= 0
        if value < 0:
            raise ValueError("height must be >= 0")

        # set height
        self.__height = value
