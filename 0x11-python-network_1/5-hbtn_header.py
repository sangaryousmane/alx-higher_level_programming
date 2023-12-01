#!/usr/bin/python3
""" Response header value #1"""
import requests
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    url = args[0]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
