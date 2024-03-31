#!/usr/bin/python3
"""takes URL, sends request and displays the value of request-is"""
import sys
import urllib.request


def req_id(url):
    """ A function to return the request-id"""

    with urllib.request.urlopen(url) as response:
        return response.headers.get('X-Request-ID')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <URL>")
        exit(1)
    idx = req_id(sys.argv[1])
    print(idx)
