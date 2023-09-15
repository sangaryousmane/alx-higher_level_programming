#!/usr/bin/python3
""" The Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ The base class for all the classes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """ an accesor for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ a mutator for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ an accesor for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ a mutator for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ an accesor for the x private field"""
        return self.__x

    @x.setter
    def x(self, value):
        """ an accesor for the x field"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, value):
        """ an accesor for the y field"""
        return self.__y

    @y.setter
    def y(self, value):
        """ a mutator for the y field"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculates the area of the rectangle"""
        return self.__width * self.__height
