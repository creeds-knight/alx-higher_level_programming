#!/usr/bin/python3
"""posts data to a url """
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: <url> <email>")
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print("Your email is:", email)
    print(response.text)
