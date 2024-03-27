#!/usr/bin/python3

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a DELETE request to the URL and display the body of the response
curl -s -X DELETE "$1"
