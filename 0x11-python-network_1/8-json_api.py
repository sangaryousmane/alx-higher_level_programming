#!/usr/bin/python3
"""This script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


def search_user(letter):
    if letter:
        payload = {'q': letter}
    else:
        payload = {'q': ''}

    response = requests.post('http://0.0.0.0:5000/search_user', params=payload)

    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_letter = sys.argv[1]
    else:
        query_letter = ""

    search_user(query_letter)
