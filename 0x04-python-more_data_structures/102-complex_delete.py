#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Delete a key with specific value in a dictionary """

    to_del = set()
    for k in a_dictionary:
        if a_dictionary[k] == value:
            to_del.add(k)
    for k in to_del:
        del a_dictionary[k]
    return {k: value for k, value in a_dictionary.items() if k not in to_del}
