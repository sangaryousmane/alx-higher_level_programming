#!/usr/bin/python3
"""  What's my status? #1"""
import requests


if __name__ == '__main__':

    res = requests.get("https://alx-intranet.hbtn.io/status")
    for line in res.text.split("\n"):
        print('Body response:')
        print('\t- type: {}'.format(type(line)))
        print('\t- content: {}'.format(line))
