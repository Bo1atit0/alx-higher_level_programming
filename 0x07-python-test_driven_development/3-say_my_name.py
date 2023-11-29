#!/usr/bin/python3

"""
a function that prints name and last name
Prototype: def say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
    prints name and last name
    Parameters:
    - first_name (str): The first name of the person.
    - last_name (str, optional): The last name of the person.
      Defaults to an empty string.

    Returns:
    str: A formatted string representing the person's name.
    If last_name is provided,
         the full name is returned; otherwise, only the first name is returned.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
