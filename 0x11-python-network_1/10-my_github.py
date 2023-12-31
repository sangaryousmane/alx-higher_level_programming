#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    args = sys.argv[1:]
    url = 'https://api.github.com/users/{}'.format(args[0])

    response = requests.get(url, auth=HTTPBasicAuth(args[0], args[1]))
    print(response.json().get('id'))
