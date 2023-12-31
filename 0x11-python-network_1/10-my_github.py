#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys
from requests.auth import HTTPBasicAuth


def get_user_id(username, password):
    url = 'https://api.github.com/users/{}'.format(username)
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print(f"Failed to fetch user ID. Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        get_user_id(username, password)
    else:
        print("Please provide both username and password")
