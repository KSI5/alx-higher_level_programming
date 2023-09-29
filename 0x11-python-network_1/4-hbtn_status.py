#!/usr/bin/python3
"""
A Python script that fetches
https://alx-intranet.hbtn.io/status using the requests package
and displays the body of the response with tabulation.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Print the response information with tabulation
        print("Body response:")
        print("    - type: {}".format(type(response.text)))
        print("    - content: {}".format(response.text))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
