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
    def y(self):
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

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print("")
        for row in range(self.__height):
            for j in range(self.x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ format the class content"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.__width}/{self.__height}"

    def update(self, *args):
        """ add variable number of no-keywords argument"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

    def to_dictionary(self):
        """ return the dictionary represention"""
        dict_rpr = {'id': self.id, 'width': self.width,
                    'height': self.height, 'x': self.x, 'y': self.y}
        return dict_rpr
