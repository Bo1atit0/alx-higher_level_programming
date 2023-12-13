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

    # Task 15
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    # Task 16
    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        json_list = []
        if list_objs is None or len(list_objs) == 0:
            with open(filename, "w") as f:
                f.write(cls.to_json_string(json_list))

        else:

            # iterate through objects
            for obj in list_objs:
                # convert objects to dictionaries
                obj_dict = cls.to_dictionary(obj)
                json_list.append(obj_dict)
            # write objects into json file
            with open(filename, "w") as f:
                f.write(cls.to_json_string(json_list))

    # Task 17
    @staticmethod
    def from_json_string(json_string):
        """
        turns the list of the JSON string
        representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    # Task 18
    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        """
        dummy_instance = cls(2, 2)
        dummy_instance.update(**dictionary)

        return dummy_instance
