#!/usr/bin/python3
""" A derive class to the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits from the base Rectangle class"""

    def __init__(self, size):
        """ the class constructor"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Implements the area function given the height and
        the width
        """
        return self.__size ** 2
