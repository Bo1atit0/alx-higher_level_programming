#!/usr/bin/python3

"""
class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)
if id is not None, id = public instance attribute id
else, increment __nb_objects and assign value to id
"""
import json
import os


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
        converts the JSON string
        representation of 'json_string' to a list
        'json_string' - a string representing a list of dictionaries
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
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = '{}.json'.format(cls.__name__)
        instance_list = []
        # if file exits, open and read from it
        if os.path.exists(filename):
            with open(filename, "r") as f:
                dictionary = f.read()
                kwargs = cls.from_json_string(dictionary)
                for value in kwargs:
                    instance_list.append(cls.create(**value))
            return instance_list
        else:
            return instance_list
