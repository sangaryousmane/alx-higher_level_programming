#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.keys():
        value *= 2
        new_dict[key] = value
    return a_dictionary
