#!/usr/bin/python3
""""
This function adds two numbers and return their sum

>>> add_integer(10, 4)
14
"""

def add_integer(a, b=98):
    """
    This function takes two arguments, a and b, and returns their sum.
    If a or b is not an integer or a float, it raises a TypeError.
    If a or b is a float, it is first cast to an integer before adding.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
