#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
and displays information about the response.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            print("Body response:")
            print("\t- type:", type(response.read()))
            print("\t- content:", response.read())
            print("\t- utf8 content:", response.read().decode("utf-8"))
    except Exception as e:
        print(e)
