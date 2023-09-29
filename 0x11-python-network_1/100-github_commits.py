#!/usr/bin/python3
"""
Lists 10 commits from the most recent to the oldest
of the repository specified by the user.
"""

import sys
import requests

if __name__ == "__main__":
    # Check if both repository name and owner name arguments were provided
    if len(sys.argv) != 3:
        sys.exit("Usage: ./list_commits.py <repository_name> <owner_name>")

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'

    try:
        request = requests.get(url)
        request.raise_for_status()  # Raise an exception for HTTP errors
        commits = request.json()

        # Ensure there are at least 10 commits
        if len(commits) < 10:
            print("Less than 10 commits available in the repository.")
        else:
            # List the 10 most recent commits
            for i in range(10):
                sha = commits[i]['sha']
                author_name = commits[i]['commit']['author']['name']
                print('{}: {}'.format(sha, author_name))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    except ValueError:
        print("Invalid JSON response from GitHub API")

