#!/usr/bin/python3
""" POST an email #1"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.post(url, data={"email": sys.argv[2]})
    print(res.text)
