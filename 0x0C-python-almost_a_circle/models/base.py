#!/usr/bin/python3
"""The parent class for all other classes"""

import csv
import json
import os
import turtle


class Base:
    """The Parent class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(pair) == dict for pair in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON representation to file,
        with the class name attached"""

        file_ = cls.__name__ + ".json"

        with open(file_, "w") as json_rpr:
            if list_objs is None:
                json_rpr.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                json_rpr.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""

        json_str = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_str = json.loads(json_string)
        return json_str

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance """

        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ File to instances"""

        file_ = cls.__name__ + ".json"
        instances = []
        _dictionaries = []

        if os.path.exists(file_):
            with open(file_, 'r') as f:
                _str = f.read()
                _dictionaries = cls.from_json_string(_str)
                for dicts in _dictionaries:
                    instances.append(cls.create(**dicts))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This method Serializes the list object and saves to file"""

        file_ = cls.__name__ + ".csv"

        with open(file_, "w", newline="") as my_csv:
            if list_objs is None or list_objs == []:
                my_csv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                write_to_csv = csv.DictWriter(my_csv, fieldnames=fields)
                for lst_obj in list_objs:
                    write_to_csv.writerow(lst_obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This class method deserializes CSV from a file"""

        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_dictionary = csv.DictReader(csvfile, fieldnames=fields)
                list_dictionary = [dict([k, int(v)] for k, v in dicts.items())
                                   for dicts in list_dictionary]
                return [cls.create(**dicts) for dicts in list_dictionary]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Update the class Base by adding the static method def
        draw(list_rectangles, list_squares): that opens a window and
        draws all the Rectangles and Squares:
        No constraints for color, and shape
        """

        shape = turtle.Turtle()
        shape.screen.bgcolor("#b7312c")
        shape.pensize(3)
        shape.pencolor((0, 10, 255))
        shape.fillcolor((255, 0, 0))
        shape.shape("turtle")
        shape.color((255, 0, 0))

        for rectangle in list_rectangles:
            shape.showturtle()
            shape.up()
            shape.goto(rectangle.x, rectangle.y)
            shape.down()

            for j in range(2):
                shape.forward(rectangle.width)
                shape.left(90)
                shape.forward(rectangle.height)
                shape.left(90)
            shape.hideturtle()

        shape.color("#b5e3d8")

        for square in list_squares:
            shape.showturtle()
            shape.up()
            shape.goto(square.x, square.y)
            shape.down()

            for j in range(2):
                shape.forward(square.width)
                shape.left(90)
                shape.forward(square.height)
                shape.left(90)
            shape.hideturtle()

        turtle.exitonclick()
