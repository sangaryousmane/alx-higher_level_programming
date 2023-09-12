#!/usr/bin/python3
""" Handles a class that inherits the list class"""


class MyList(list):
    """ Inherits from the list class"""
    pass

    def print_sorted(self):
        """ Prints a list in sorted ascending form"""
        print(f'{sorted(self)}')
