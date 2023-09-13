#!/usr/bin/python3
""" emulates a student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ Construct the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def def to_json(self):
        """ converts from class to json"""
        obj_dict = self.__dict__

        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                continue
            elif isinstance(value, set):
                obj_dict[key] = list(value)
            else:
                obj_dict[key] = str(value)
        return obj_dict
