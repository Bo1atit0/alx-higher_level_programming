#!/usr/bin/python3

"""
a function that returns true
if object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Function that checks if obj is an instance of a class
    inherited from a_class (directly or indirectly).
    
    Return: True or False
    """
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
