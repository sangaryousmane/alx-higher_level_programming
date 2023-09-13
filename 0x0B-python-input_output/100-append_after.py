#!/usr/bin/python3
""" inserts a line of text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file,
    after each line containing a specific string """

    lines = ""
    with open(filename) as r:
        for line in r:
            lines += line
            if search_string in line:
                lines += new_string
    with open(filename, "w") as f:
        f.write(lines)
