#!/usr/bin/python3
"""appends a string at the end of a text file(UTF8) and
returns the number of characters written
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a") as f:
        data = f.write(text)
        return data
