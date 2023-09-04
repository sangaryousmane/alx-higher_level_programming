#!/usr/bin/python3
""" Defines a Rectangle class"""


class Rectangle:
    """
    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a new constructor.
    - width(self): Returns the width of the rectangle.
    - width(self, value): Sets the width of the rectangle
    - height(self): Returns the height of the rectangle.
    - height(self, value): Sets the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not of type int
            ValueError: if size is negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width's value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ The heigth's mutator """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
