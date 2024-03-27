#!/bin/bash
# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL and store the response in a temporary file
response=$(mktemp)
curl -s -o "$response" -w '%{size_download}' "$1"

# Display the size of the response body in bytes
cat "$response"

# Clean up the temporary file
rm "$response"
