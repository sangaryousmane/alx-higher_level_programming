#!/usr/bin/python3
""" The Rectangle's top-level doc """


class Rectangle:
    """
    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): the constructor
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of a rectangle given its width and height

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle given its width and height.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
        """
        result = 0
        if self.__width == 0 or self.__height == 0:
            result = 0
        else:
            result = 2 * (self.__width + self.__height)
        return result

    def __str__(self):
        """ Returns a string representation of the rectangle class"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for col in range(self.__height):
            for row in range(self.__width):
                rect += "#"
            if col < (self.__height - 1):
                rect += "\n"
        return rect

    def __repr__(self):
        """
        Returns a string representation of the rectangle to recreate the object
        Returns:
        str: A string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print(f'Bye rectangle...')
