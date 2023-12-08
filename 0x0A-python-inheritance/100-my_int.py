#!/usr/bin/python3

class MyInt(int):
    """
    a class inheriting from the built-in int class
    """
    # def __init__(self, value):
    # self.value = value

    def __eq__(self, other):

        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
