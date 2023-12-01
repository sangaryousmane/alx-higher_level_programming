#!/usr/bin/python3
""" Error code #0"""
from urllib.request import urlopen
import sys
from urllib.error import HTTPError


if __name__ == '__main__':
    args = sys.argv[1:]
    url = args[0]

    try:
        with urlopen(url) as res:
            print(res.read().decode('ascii'))
    except HTTPError as err:
        print(f"Error code: {err.code}")
