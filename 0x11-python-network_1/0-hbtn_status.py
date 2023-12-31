#!/usr/bin/python3
""" What's my status? #0"""
from urllib.request import urlopen


if __name__ == '__main__':
    with urlopen("https://alx-intranet.hbtn.io/status") as res:
        page = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
