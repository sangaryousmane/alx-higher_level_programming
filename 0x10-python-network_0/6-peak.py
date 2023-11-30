#!/usr/bin/python3
""" Peek in an unsorted ints array"""


def find_peak(list_of_integers):
    """ Find the peak element in an unsorted array"""
    if list_of_integers == []:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    end = len(list_of_integers) - 1
    start = 0

    while start < end:
        middle = start + (end - start) // 2

        if list_of_integers[middle] > list_of_integers[middle + 1]:
                end = middle
        else:
            start = middle + 1
    return list_of_integers[start]

