#!/usr/bin/python3
def weight_average(my_list=[]):

    """ Calculate the weighted average """
    if my_list:
        up = sum((tup1[0] * tup1[1]) for tup1 in my_list)
        down = sum(tup1[1] for tup1 in my_list)
        return (up / down);
    return (0);
