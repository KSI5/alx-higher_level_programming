#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes.

# Send a GET request to the provided URL and use curl's -s (silent) and -o (output) options
curl -s -o /tmp/body_size_response "$1"

# Use the 'stat' command to get the size of the downloaded file (response body)
body_size=$(stat -c %s /tmp/body_size_response)

# Display the size in bytes
echo "$body_size"
