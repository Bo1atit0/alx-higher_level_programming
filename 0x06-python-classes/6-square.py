#!/usr/bin/python3

"""
Class Square:
    This class defines a square with size,
    position, and methods to calculate area and print the square.

Attributes:
    __size (int): The size of the square.
    __position (tuple): The position of the square.

Methods:
    __init__(self, size=0, position=(0, 0)): Initializes a new Square instance.
    size(self): Getter method to retrieve the size.
    size(self, value): Setter method to set the size.
    position(self): Getter method to retrieve the position.
    position(self, value): Setter method to set the position.
    area(self): Calculates and returns the area of the square.
    my_print(self): Prints the square using "#".
"""


class Square:
    """
    Instantiating the variables self and size.
    Raising errors if conditions are not met.
    and print square using '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If `value` is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates area of a square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square using '#'.
        """
        if self.__size == 0:
            print()
            return
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
