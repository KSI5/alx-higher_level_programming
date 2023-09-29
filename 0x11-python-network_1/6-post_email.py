#!/usr/bin/python3
"""
A Python script that sends a POST request to a URL with an email parameter
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if both URL and email arguments were provided
    if len(sys.argv) != 3:
        sys.exit("Usage: ./post_email.py <URL> <email>")

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = {'email': email}

    try:
        response = requests.post(url, data=data)

        # Check for successful response (status code 200)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: Status code", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
