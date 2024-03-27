#!/usr/bin/python3
# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL with the custom header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
