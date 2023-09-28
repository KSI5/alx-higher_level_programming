#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me and extracts the message

# Send the request and write the response to a file
curl -s 0.0.0.0:5000/catch_me -o response.txt

# Use grep to extract the message
grep -o "You got me!" response.txt
