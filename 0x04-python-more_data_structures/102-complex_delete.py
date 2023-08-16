#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            to_del.append(k)
    for k in to_del:
        del a_dictionary[k]
    return a_dictionary
