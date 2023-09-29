#!/usr/bin/python3
"""
A Python script that takes GitHub credentials (username and personal access token)
and uses Basic Authentication to access the GitHub API and display your GitHub User ID.

Requirements:
- Use the requests package.
- Do not import any packages other than requests and sys.

Usage:
./github_user_id.py <username> <personal_access_token>
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Check if both username and personal access token arguments were provided
    if len(sys.argv) != 3:
        sys.exit("Usage: ./github_user_id.py <username> <personal_access_token>")

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    # Construct the GitHub API URL to fetch user information
    url = f"https://api.github.com/user"

    # Create Basic Authentication
    auth = HTTPBasicAuth(username, personal_access_token)

    try:
        # Send a GET request to the GitHub API
        response = requests.get(url, auth=auth)
        response.raise_for_status()  # Raise an exception for HTTP errors
        user_data = response.json()

        # Check if the response contains user information
        if 'id' in user_data:
            user_id = user_data['id']
            print(f"GitHub User ID: {user_id}")
        else:
            print("User information not found")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    except ValueError:
        print("Invalid JSON response from GitHub API")

