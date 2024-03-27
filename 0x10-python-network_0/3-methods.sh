#!/usr/bin/python3
# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send an OPTIONS request to the URL and display the allowed methods
curl -s -X OPTIONS -I "$1" | grep "Allow" | cut -d ' ' -f 2-
