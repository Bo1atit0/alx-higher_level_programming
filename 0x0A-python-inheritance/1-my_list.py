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
    def __init__(self):
        """
        initializes the class
        """
        super().__init__(self)

    def print_sorted(self):
        """
        prints the list, but sorted
        """
        sorted_list = sorted(self)
        print(sorted_list)
