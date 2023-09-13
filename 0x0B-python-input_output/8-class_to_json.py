#!/usr/bin/python3
""" converts a class to an object"""


def class_to_json(obj):
    """ converts from class to json"""
    obj_dict = obj.__dict__

    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            continue
        elif isinstance(value, set):
            obj_dict[key] = list(value)
        else:
            obj_dict[key] = str(value)
    return obj_dict
