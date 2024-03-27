#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL and store the response in a temporary file
response=$(mktemp)
status_code=$(curl -s -o "$response" -w "%{http_code}" "$1")

# Check if the response status code is 200 (OK)
if [ "$status_code" -eq 200 ]; then
  # Display the body of the response
  cat "$response"
else
  echo "Error: HTTP status code $status_code"
fi

# Clean up the temporary file
rm "$response"
