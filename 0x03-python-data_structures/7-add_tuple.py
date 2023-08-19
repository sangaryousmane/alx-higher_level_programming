#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    This function adds 2 tuples. zip() takes two tuples
    as arguments and perform addition on them using the
    map() higher order function. Finally, the tuple()
    converts the operation to tuples and return it.
    """

    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    sum_tuple = tuple(map(sum, zip(tuple_a, tuple_b)))
    return added_tuple
