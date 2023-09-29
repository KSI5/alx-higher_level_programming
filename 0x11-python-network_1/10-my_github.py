#!/usr/bin/python3
"""
A Python script that takes GitHub credentials
(username and personal access token)
and uses Basic Authentication to access the
GitHub API and display your GitHub User ID.

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
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
