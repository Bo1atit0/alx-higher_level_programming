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
        """
        initializes the rectangle class
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
