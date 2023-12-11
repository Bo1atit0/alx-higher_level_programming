#!/usr/bin/python3

"""
is_same_class module
function that returns True if the object
is exactly an instance of the specified class;
otherwise False
"""


def is_same_class(obj, a_class):
    """
    checks if type(obj) is true
    or false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
