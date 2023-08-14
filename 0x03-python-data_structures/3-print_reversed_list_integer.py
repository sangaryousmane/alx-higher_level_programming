#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    """ Print list in reverse """
    if my_list:
        reverse = my_list[::-1]
        for item in reverse:
            print("{:d}".format(item))
