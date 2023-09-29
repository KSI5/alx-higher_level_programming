#   0x11-python-network_1 🌐

This collection of Python scripts demonstrates various network-related tasks, including making HTTP requests, handling responses, and working with APIs.

## Table of Contents 📑

1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Tasks](#tasks)
    - [Task 0: What's my status? #0](#task-0-whats-my-status-0---0-hbtn_statuspy)
    - [Task 1: Response header value #0](#task-1-response-header-value-0---1-hbtn_headerpy)
    - [Task 2: POST an email #0](#task-2-post-an-email-0---2-post_emailpy)
    - [Task 3: Error code #0](#task-3-error-code-0---3-error_codepy)
    - [Task 4: What's my status? #1](#task-4-whats-my-status-1---4-hbtn_statuspy)
    - [Task 5: Response header value #1](#task-5-response-header-value-1---5-hbtn_headerpy)
    - [Task 6: POST an email #1](#task-6-post-an-email-1---6-post_emailpy)
    - [Task 7: Error code #1](#task-7-error-code-1---7-error_codepy)
    - [Task 8: Search API](#task-8-search-api---8-json_apipy)
    - [Task 10: My GitHub!](#task-10-my-github---10-my_githubpy)
    - [Advanced Task: Time for an interview!](#advanced-task-time-for-an-interview-100-github_commitspy)
4. [Requirements](#requirements)
5. [Usage](#usage)
6. [Repository](#repository)

## Introduction 📜

This repository contains Python scripts that cover a range of topics related to web requests and data retrieval.

## Learning Objectives 🧠

By completing the tasks in this repository, you will be able to:

- Learn how to fetch internet resources using the Python package `urllib`.
- Understand how to decode the body of a response from `urllib`.
- Utilize the Python package `requests` for making HTTP requests.
- Make HTTP GET requests to retrieve data from web resources.
- Make HTTP POST/PUT/etc. requests for various operations.
- Fetch and handle JSON resources from external services.
- Manipulate data retrieved from external services.

## Tasks 📋

### Task 0: What's my status? #0 - `0-hbtn_status.py`
- Write a Python script that fetches a specific URL using the `urllib` package.
- Display the type, content, and decoded content of the response.

### Task 1: Response header value #0 - `1-hbtn_header.py`
- Create a Python script that sends a request to a specified URL.
- Display the value of the `X-Request-Id` variable found in the header of the response.

### Task 2: POST an email #0 - `2-post_email.py`
- Develop a Python script that sends a POST request to a URL with an email as a parameter.
- Display the body of the response (decoded in utf-8).

### Task 3: Error code #0 - `3-error_code.py`
- Write a Python script that sends a request to a URL and displays the body of the response (decoded in utf-8).
- Handle `urllib.error.HTTPError` exceptions and print the HTTP status code in case of an error.

### Task 4: What's my status? #1 - `4-hbtn_status.py`
- Similar to Task 0, fetch a specific URL using the `urllib` package.
- Display the type, content, and decoded content of the response.

### Task 5: Response header value #1 - `5-hbtn_header.py`
- Similar to Task 1, send a request to a specified URL.
- Display the value of the `X-Request-Id` variable found in the header of the response.

### Task 6: POST an email #1 - `6-post_email.py`
- Similar to Task 2, send a POST request to a URL with an email as a parameter.
- Display the body of the response (decoded in utf-8).

### Task 7: Error code #1 - `7-error_code.py`
- Similar to Task 3, send a request to a URL and display the body of the response (decoded in utf-8).
- Handle `urllib.error.HTTPError` exceptions and print the HTTP status code in case of an error.

### Task 8: Search API - `8-json_api.py`
- Implement a Python script that searches an API for data and handles the response.

### Task 10: My GitHub! - `10-my_github.py`
- Write a Python script that uses the GitHub API to display your GitHub User ID.
- Utilize Basic Authentication with a personal access token.

## Advanced Task: 💪
- Time for an interview! - `100-github_commits.py`
- List the 10 most recent commits (from the most recent to oldest) of a specified GitHub repository by the user.
- Utilize the GitHub API to retrieve and display the commit information.
- Accept two command-line arguments: the repository name and the owner name.

## Requirements 📝

- Allowed editors: vi, vim, emacs.
- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- All modules should have proper documentation.
- The code should not be executed when imported (using `if __name__ == "__main__":`).

## Usage 🚀

To run the scripts, execute them in your terminal with appropriate command-line arguments. For example:

```bash
./0-hbtn_status.py
./1-hbtn_header.py https://alx-intranet.hbtn.io
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./3-error_code.py http://0.0.0.0:5000
./list_commits.py rails rails

