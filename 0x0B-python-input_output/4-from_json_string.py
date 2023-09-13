#!/usr/bin/python3
""" Derializes a python string"""
import json


def from_json_string(my_str):
    """ Derializes json object"""
    return json.loads(my_str)
