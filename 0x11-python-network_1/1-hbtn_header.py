#!/usr/bin/python3
""" Response header value #0 """
from urllib.request import urlopen
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    url = args[0]
    with urlopen(url) as res:
        headers = res.headers
        x_request_id = headers.get("X-Request-Id")
        print(f'{x_request_id}')
