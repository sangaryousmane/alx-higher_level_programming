#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

""" Test case for the Base class of all classes"""


class TestBase(unittest.TestCase):
    """ Test for the Base class """

    def test_id_is_none(self):
        """ is Id none"""
        base = Base()
        self.assertEqual(1, base.id)

    def test_valid_id(self):
        """ Case to test valid ID"""
        base = Base(50)
        self.assertEqual(50, base.id)

    def test_when_id_is_zero(self):
        """ testing zero case"""
        base = Base(0)
        self.assertEqual(0, base.id)

    def test_id_is_negative(self):
        """ testing negative case"""
        base = Base(-1)
        self.assertEqual(-1, base.id)

    def test_id_is_string(self):
        """ Testing a a non-integer ID"""
        base = Base("pycode")
        self.assertEqual("pycode", base.id)

    def test_id_is_list(self):
        """test if id is list"""
        base = Base([1, 3, 10, 15])
        self.assertEqual([1, 3, 10, 15], base.id)

    def test_id_is_dict(self):
        """ Testing if Id is a dictionary"""
        base = Base({"id": 2220551207})
        self.assertEqual({"id": 2220551207}, base.id)

    def test_id_is_tuple(self):
        """ Test for tuple"""
        base = Base((9, 1))
        self.assertEqual((9, 1), base.id)

    def test_json_type(self):
        """ testing the string to json case"""
        square = Square(1)
        to_dict = square.to_dictionary()
        to_str = Base.to_json_string([to_dict])
        self.assertEqual(type(to_str), str)

    def test_to_json_value(self):
        """ json value"""
        square = Square(3, 10, 10, 30)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        dicts_ = {"id": 30, "y": 10, "x": 10, "size": 3}
        self.assertEqual(json.loads(json_string), dicts_)

    def test_to_json_None(self):
        """ the json is None case"""
        square = Square(3, 10, 10, 30)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """  Emtpty json case"""
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_str = Base.to_json_string([])
        self.assertEqual(json_sr, "[]")


class TestBaseClassMethods(unittest.TestCase):
    """ For testing methods belongging to the base class"""

    @classmethod
    def setUpClass(cls):
        """
        Set up
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_and_class_docstring(self):
        """
        Test for class docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Test for the existence of the moule docstring documntation
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
