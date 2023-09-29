#!/usr/bin/python3
"""
A Python script that sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter and processes the response.

Requirements:
- Use the requests package.
- Do not import any packages other than requests and sys.

Usage:
./search_user.py <letter>
"""

import sys
import requests

if __name__ == "__main__":
    # Check if a letter argument was provided, default to empty string if not
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            print("[{}] {}".format(response_json['id'], response_json['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
