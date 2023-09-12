#!/usr/bin/python3
""" Mimics a base class geometry"""


class BaseGeometry:
    """ Serve as super class for future child classes"""

    def area(self):
        """ Raise an exception"""
        raise Exception("area() is not implemented")
