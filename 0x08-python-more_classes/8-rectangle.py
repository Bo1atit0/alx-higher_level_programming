#!/usr/bin/python3
"""
 a class Rectangle that defines a rectangle
private instance attribute: width, height
Raises: errors if conditions are not met
"""


class Rectangle:
    """
    instantiating variales width and height
    Parameters:
                width
                height
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        # get width
        return self.__width

    @width.setter
    def width(self, value):
        # make sure width is an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")

        # width must be >= 0
        if value < 0:
            raise ValueError("width must be >= 0")
        # set width
        self.__width = value

    @property
    def height(self):
        # get height
        return self.__height

    @height.setter
    def height(self, value):
        # height must be an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")

        # height >= 0
        if value < 0:
            raise ValueError("height must be >= 0")

        # set height
        self.__height = value

    def area(self):
        # calculates the area of a rectangle
        return self.__width * self.__height

    def perimeter(self):
        # calculates perimeter of a rectangle
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        print rectangles with '#'
        """
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            rect_str = ""
        else:
            for _ in range(self.__height):
                rect_str += str(self.print_symbol) * self.__width + '\n'
        return rect_str[:-1]

    def __repr__(self):
        """
        return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """

        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        called when an object is about to be deleted
        prints message
        """
        print("Bye rectangle...")

        # decrement rectangle population
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        method that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 >= area2:
            return rect_1
        else:
            return rect_2
