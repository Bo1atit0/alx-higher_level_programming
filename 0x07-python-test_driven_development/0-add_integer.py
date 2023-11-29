#!/usr/bin/python3
"""
add_integer: add two integers or floats
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Raises:
    TypeError: If a or b is not an int or a float.

    Returns:
    int or float: The sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)
    return a + b
