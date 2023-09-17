#!/usr/bin/pytho3
""" Mimic the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the quare class extends the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ The class's constructor"""
        self.size = self.width
        self.size = self.height
        super().__init__(self, size, x, y)

    def __str__(self):
        """ return a formatted string"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """ getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """ setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        self.__height = value
