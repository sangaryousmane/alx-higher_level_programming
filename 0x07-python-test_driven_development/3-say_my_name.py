#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    This function takes two arguments, first_name and last_name,
    and prints the person's full name.
    If first_name or last_name is not a string, it raises a TypeError
    with a message indicating which argument is not a string.

    Args:
      first_name (str): The person's first name.
      last_name (str): The person's last name. Defaults to an empty string.

    Returns:
      None
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
