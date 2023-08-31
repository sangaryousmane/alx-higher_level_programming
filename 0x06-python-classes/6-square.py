#!/usr/bin/python3
"""Emulates a square"""


class Square:
    """This class implements a  Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """this is the class constructor
        Args:
         size: the input size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    def area(self):
        """ Calculate the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """ a public setter metter to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ the mutator that set a size for us"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square with #"""
        post = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            post += "\n"
        for j in range(self.size):
            for k in range(self.position[0]):
                post += " "
            for w in range(self.size):
                post += "#"
            post += "\n"
        print(f'{post}', end='')
