#!/usr/bin/python3

"""
class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)
if id is not None, id = public instance attribute id
else, increment __nb_objects and assign value to id
"""
import json


class Base:
    """
    A Base class
    the base of all other classes
    manages id attribute for all clases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)
