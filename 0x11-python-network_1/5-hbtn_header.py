#!/usr/bin/python3
"""
A Python script that takes a URL as input, sends
a GET request to the URL and displays the value of the
'X-Request-Id' variable found in the response header.

Requirements:
- You must use the package 'requests'.
- No other packages should be imported.

Usage:
./get_x_request_id.py <URL>
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
