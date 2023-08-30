#!/usr/bin/python3
""" Square instance """


class Square:
    """Square instance"""

    def __init__(self, size=0):
        """ The constructor"""

        if type(size) != int or type(size) != int:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ the size's accessor"""

        return self.__size

    @size.setter
    def size(self, value):
        """the size mutator """

        if type(value) != int or type(value) != int:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ find the area of the square"""
        return self.__size * self.__size

    def __le__(self, foreign):
        return self.area() <= foreign.area()

    def __lt__(self, foreign):
        return self.area() < foreign.area()

    def __ge__(self, foreign):
        return self.area() >= foreign.area()

    def __ne__(self, foreign):
        return self.area() != foreign.area()

    def __gt__(self, foreign):
        return self.area() > foreign.area()

    def __eq__(self, foreign):
        return self.area() == foreign.area()
