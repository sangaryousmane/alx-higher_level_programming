#!/usr/bin/python3
""" Inherits from the in class and invert its equal
and not equal methods"""


class MyInt(int):
    """
    A subclass of the built-in int class that inverts
    the == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to return the opposite
        of the built-in behavior.

        Args:
            other: An object to compare against.

        Returns:
            bool: True if the objects are not equal; otherwise, False.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to return the opposite of
        the built-in behavior.

        Args:
            other: An object to compare against.

        Returns:
            bool: True if the objects are equal; otherwise, False.
        """
        return not super().__ne__(other)
