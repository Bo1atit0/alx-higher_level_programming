#!/usr/bin/python3

"""
a base-geometry class
Public instance method: def area(self)
Public instance method:
def integer_validator(self, name, value)

"""


class BaseGeometry:
    """
    Public instance method: def area(self):
    raises an Exception with the message
    area() is not implemented
    """

    def area(self):
        """
        raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        a method that validate value
        you can assume name is always a string
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
