#!/usr/bin/python3

"""
Rectangle class module that inherits from Base
Private instance attributes:
__width
__height
__x
__y
Class constructor:
def __init__(self, width, height, x=0, y=0, id=None)

"""

from models.base import Base


# Task 2: write a class rectangle
class Rectangle(Base):
    """
    Defines a Rectangle class that inherits from the
    Base class
    Inherited attributes:
            id
    Class attributes:
             width, height, x, y
    Public methods:
            area(), display(), update()
    """
    # Task 3: Validate all setter methods and Instantiation
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)   # call the parent class
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    # getter and setter for WIDTH
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    # getter and setter for HEIGHT
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    # getter and setter for X
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    # getter and setter for Y
    @property
    def y(self):

        return self.__y

    @y.setter
    def y(self, new_y):
        """
        value setter for y
        """
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    # Task 4
    def area(self):
        """
        area method: returns the area of a rectangle
        """

        return self.__width * self.__height

    # Task 5
    def display(self):
        """
        displays the rectangle using '#' character
        """
        [print() for _ in range(self.__y)]
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    # Task 6 and 7
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    # Task 8(*args) and 9(**kwargs)
    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by using *args
        to assigns  arguments to each attribute
        Update the class Rectangle by using **kwargs to
        assigns a key/value argument to the attributes
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if kwargs:
                keys = {"id", "width", "height", "x", "y"}
                for key, value in kwargs.items():
                    if key in keys:
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation
        of a Rectangle
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
