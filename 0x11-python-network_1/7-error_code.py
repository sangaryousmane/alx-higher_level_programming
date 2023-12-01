#!/usr/bin/python3
""" Error code using resquests library"""
import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        err_code = res.status_code
        print(f"Error code: {err_code}")
    else:
        print(res.text)
