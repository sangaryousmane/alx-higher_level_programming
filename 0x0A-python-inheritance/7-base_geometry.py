#!/usr/bin/python3
""" Mimics a base class geometry"""


class BaseGeometry:
    """ Serve as super class for future child classes"""

    def area(self):
        """ Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates an integer"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
