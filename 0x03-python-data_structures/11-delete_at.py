#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    """ Delete an element at a specific index"""

    if my_list:
        if idx < 0 or idx >= len(my_list):
            return (my_list)
        else:
            my_list.remove(idx)
    return (my_list)
