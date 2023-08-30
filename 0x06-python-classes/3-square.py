#!/usr/bin/python3
"""Emulates a square"""


class Square:
    """This class implements a  Square that defines a square"""

    def __init__(self, size=0):
        """this is the class constructor
        Args:
         size: the input size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculate the area of the square"""
        return self.__size * self.__size
