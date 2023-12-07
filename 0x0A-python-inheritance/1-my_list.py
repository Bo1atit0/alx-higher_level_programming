#!/usr/bin/python3

"""
a class MyList that inherits from list built_in -
- data type(class)
def print_sorted(self): that prints the list,
but sorted
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
