#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_list = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del_list.append(key)
    for key in del_list:
        del a_dictionary[key]
    return a_dictionary
