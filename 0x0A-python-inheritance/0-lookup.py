#!/usr/bin/python3
""" Returns the list of available attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of the names of the attributes and methods of an object.
    Args:
        obj: An object to inspect.
    Returns:
        list: A list of strings representing the names of the -
        attributes and methods of the object.
    """
    return dir(obj)
