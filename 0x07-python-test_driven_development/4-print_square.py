#!/usr/bin/python3

"""
Print Square module
The module prints a square with `#`

size: size length of the square
Raise exceptions:
  if size is not an int, or if size is less than 0,
  or if size is a float and also less than 0.
"""


def print_square(size):
    """
     prints a square with '#'
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
