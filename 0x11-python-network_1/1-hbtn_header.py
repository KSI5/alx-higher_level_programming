#!/usr/bin/python3
"""
A Python script that sends a request to a URL and displays the value
of the X-Request-Id variable found in the response header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Check if a URL argument was provided
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-hbtn_header.py <URL>")

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Check if the 'X-Request-Id' header is present in the response
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response")

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
