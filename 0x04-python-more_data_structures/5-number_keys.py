#!/usr/bin/python3
def number_keys(a_dictionary):
    """ Returns the number of keys in a dictionary """
    count = 0
    for key, value in a_dictionary.items():
        count += 1
    return count
