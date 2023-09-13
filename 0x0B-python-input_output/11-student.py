#!/usr/bin/python3
""" emulates a student"""


class Student:
    """ The student class"""

    def __init__(self, first_name, last_name, age):
        """ Construct the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """ Reload from json"""
        for key, value in json.items():
            setattr(self, key, value)
