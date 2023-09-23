#!/usr/bin/python3
""" Finds the sum of two"""


def add_integer(a, b=98):
    """
    This function takes two arguments, a and b, and returns their sum.
    If a or b is not an integer or a float, it raises a TypeError.
    If a or b is a float, it is first cast to an integer before adding.
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
