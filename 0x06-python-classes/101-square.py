#!/usr/bin/python3
"""my square module."""


class Square:
    """define a Square."""

    def __str__(self):
        """ print the square """
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ initialize the square with this
        Args:
            size: a side of square
            position: the position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property of the length of a side of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of square"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if type(value) != tuple(int, int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if type(i) == int and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ the area of square"""
        return self.__size * self.__size

    def pos_print(self):
        """returns the printed square with position"""
        post = ""
        if not self.size:
            return "\n"
        for j in range(self.position[1]):
            post += "\n"
        for j in range(self.size):
            for i in range(self.position[0]):
                post += " "
            for k in range(self.size):
                post += "#"
            post += "\n"
        return post

    def my_print(self):
        """print square."""
        print(self.pos_print(), end="")
