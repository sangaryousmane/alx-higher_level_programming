#!/usr/bin/python3
""" The Base class"""


class Base:
    """ THe base class for all the classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructs our class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
