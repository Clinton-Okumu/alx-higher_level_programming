#!/usr/bin/python3
# Send a POST request to the URL with the specified variables and display the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
