#!/usr/bin/python3
"""
A Python script that fetches
https://alx-intranet.hbtn.io/status using the requests package
and displays the body of the response with tabulation.
"""

import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
