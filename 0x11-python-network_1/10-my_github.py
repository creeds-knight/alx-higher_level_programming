#!/usr/bin/python3
""" Takes github credentials and uses github api to display id"""
import sys
import requests

def git_hub_id(username, password):
    """ A function to return git hub id"""

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print(data['id'])
    else:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    git_hub_id(username, password)
