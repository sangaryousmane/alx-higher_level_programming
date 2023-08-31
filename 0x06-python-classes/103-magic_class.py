#!/usr/bin/python3
"""A magic class for python bytecode"""
from math import pi


class MagicClass:
    """the magic class"""

    def __init__(self, radius=0):
        """ magic's class constructor """
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """finds the area"""
        return pow(self.__radius, 2) * pi

    def circumference(self):
        """finds the circumference"""
        return 2 * math.pi * self.__radius
