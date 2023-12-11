#!/usr/bin/python3

"""
 a class Rectangle that inherits from BaseGeometry
 Instantiation with width and height:
 def __init__(self, width, height):
 width and height must be private
 width and height must be positive integers,
 validated by integer_validator
"""


# Import 7-base_geometry.py module
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a rectangle class
    Inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
