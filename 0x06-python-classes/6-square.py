#!/usr/bin/python3

"""
class Square that defines a square
Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:

Private instance attribute: position
which takes a default (0, 0) tuple.
property def position(self): to retrieve it
property setter def position(self, value): to set it:

And a Public instance method: def area(self):
that returns the current square area
Method my_print prints the square using "#".
"""


class Square:
    """
    Instantiating the variables self and size.
    Raising errors if conditions are not met.
    and print square using '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """method that sets the size
        Args:
            int: size
        raises:
            TypeError
            ValueError

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """a method that sets the position of a square
        Args:
            value(tuple): 2 positive integers
        Raises:
            TypeError

        """
        if (not isinstance(value, tuple)) or (len(value) != 2)
        or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        calculates area of a square
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
