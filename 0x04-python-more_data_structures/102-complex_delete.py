#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Delete a key with specific value in a dictionary """

    to_del = set()
    for key in a_dictionary:
        if a_dictionary[key] == value:
            to_del.add(key)
    for key in to_del:
        del a_dictionary[key]
    return a_dictionary
