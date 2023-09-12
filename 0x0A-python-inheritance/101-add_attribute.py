#!/usr/bin/python3
""" adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """ Adds a new attribute to an object if it's possible.

    Args:
        obj: An object to add the attribute to.
        attr: A string representing the name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes.

    Return:
      None
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
