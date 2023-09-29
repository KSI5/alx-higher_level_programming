#!/usr/bin/python3
"""
A Python script that sends a POST request to a URL with an email parameter
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Check if both URL and email arguments were provided
    if len(sys.argv) != 3:
        sys.exit("Usage: ./2-post_email.py <URL> <email>")

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(req) as response:
            # Read and decode the response body in utf-8
            response_content = response.read().decode('utf-8')
            print(response_content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
