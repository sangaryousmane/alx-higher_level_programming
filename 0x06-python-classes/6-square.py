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
        if type(position) != tuple(int, int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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
        """ Prints a square with # for us"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def position(self):
        """ Retrive the value of the private position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the value of the position variable"""
        if type(position) != tuple(int, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
