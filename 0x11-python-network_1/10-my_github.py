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

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print(f"Failed to fetch user ID. Status code: {response.status_code}")
