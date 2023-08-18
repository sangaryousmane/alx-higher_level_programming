#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set
    The symmetric difference returns capture all elements
    present in only one of the two sets(set_1 and set_2)
    """
    return set_1.symmetric_difference(set_2)
