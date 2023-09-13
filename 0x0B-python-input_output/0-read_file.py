#!/usr/bin/python3
""" reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ Reads and prints the file content to stdout"""
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end='')
