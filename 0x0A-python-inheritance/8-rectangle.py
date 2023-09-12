#!/usr/bin/python3
""" A derive class to the geometry class"""
from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from the base Geometry class"""

    def __init__(self, width, height):
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height
