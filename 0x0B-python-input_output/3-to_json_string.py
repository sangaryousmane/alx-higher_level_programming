#!/usr/bin/python3
""" Serializes a json object"""
import json


def to_json_string(my_obj):
    """ Serializes json object"""
    return json.dumps(my_obj)
