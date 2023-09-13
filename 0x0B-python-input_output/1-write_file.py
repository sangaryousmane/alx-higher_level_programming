#!/usr/bin/python3
"""writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Writes a string to a text fille"""
    with open(filename, "w") as f:
        data = f.write(text)
        return data
