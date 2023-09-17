#!/usr/bin/pytho3
""" Mimic the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the quare class extends the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ The class's constructor"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

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

    def update(self, *args, **kwargs):
        """ the update version of the square"""
        def set_attribute(attr, value):
            """ a helper inner function to minimize code"""
            if value is not None and type(value) == int :
                setattr(self, attr, value)
            else:
                raise TypeError("id must be an integer")

        if args:
            if len(args) > 0:
                set_attribute('id', args[0])
            if len(args) > 1:
                set_attribute('width', args[1])
            if len(args) > 2:
                set_attribute('height', args[2])
            if len(args) > 3:
                set_attribute('x', args[3])
            if len(args) > 4:
                set_attribute('y', args[4])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    set_attribute('id', value)
                if key == "width":
                    set_attribute('width', value)
                if key == "height":
                    set_attribute('height', value)
                if key == "x":
                    set_attribute('x', value)
                if key == "y":
                    set_attribute('y', value)
