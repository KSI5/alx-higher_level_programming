#!/usr/bin/python3
"""
A Python script that takes a URL as input, sends a request to
the URL, and display the response body (decoded in utf-8).

Requirements:
- You must use the packages urllib and sys.
- Handle urllib.error.HTTPError exceptions and print
- the associated HTTP status code.

Usage:
./3-error_code.py <URL>
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
    except Exception as e:
        pass
