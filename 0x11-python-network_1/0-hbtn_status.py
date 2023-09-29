#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
and displays information about the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
