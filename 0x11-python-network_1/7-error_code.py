#!/usr/bin/python3
"""
A Python script that takes a URL as input, sends a GET request
to the URL using the requests package,
and displays the body of the response.

Requirements:
- You must use the requests package.
- Do not import any packages other than requests.

Usage:
./fetch_response_body.py <URL>
"""

import sys
import requests

if __name__ == "__main__":
    # Check if a URL argument was provided
    if len(sys.argv) != 2:
        sys.exit("Usage: ./fetch_response_body.py <URL>")

    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
