#!/usr/bin/python3
""" A derive class to the geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from the base Geometry class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Implements the area function given the height and
        the width
        """
        return self.__height * self.__width

    def __str__(self):
        """ the to string method for informally printing
        strings
        """
        rect = "[" + str(self.__class__.__name__) + "] "
        rect += str(self.__width) + "/" + str(self.__height)
        return rect
