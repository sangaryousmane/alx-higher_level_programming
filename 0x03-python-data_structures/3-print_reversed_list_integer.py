#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    """ Print list in reverse """
    reverse = my_list[::-1]
    if reverse:
        for item in reverse:
            print("{:d}".format(item))
