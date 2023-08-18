#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    The function used a one line list comprehension to check replace
    the old element in the list(my_list)
    """
    return [replace if search == item else item for item in my_list]
