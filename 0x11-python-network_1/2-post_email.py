#!/usr/bin/python3
""" POST an email #0"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    url = args[0]
    email = args[1]
    data = urlencode({'email': email}).encode('utf-8')
    req = Request(url, data=data, method='POST')

    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
