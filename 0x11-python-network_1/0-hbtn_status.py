#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
and displays information about the response.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        # Read the response content as bytes
        response_content_bytes = response.read()

    # Decode the response content to utf-8
    response_content_utf8 = response_content_bytes.decode("utf-8")

    # Print the response information with tabulation
    print("Body response:")
    print("    - type: {}".format(type(response_content_bytes)))
    print("    - content: {}".format(response_content_bytes))
    print("    - utf8 content: {}".format(response_content_utf8))
