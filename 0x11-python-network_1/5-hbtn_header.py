#!/usr/bin/python3
""" Sends a request to URL and displays the value of the variable
    X-request-id in the response header
"""
import requests
import sys


def get_res_id(url):
    """ A function that sends a request and prints the response id"""

    data = requests.get(url)
    idx = data.headers.get('X-Request-Id')
    print(idx)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:<url>")
        sys.exit(1)
    url = sys.argv[1]
    get_res_id(url)
