#!/usr/bin/python3
""" sends a reequest to the url and displays the body of the response """
import sys
import urllib.request
import urllib.error


def get_req(url):
    """ sends a url request and displays the body"""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            print(data)
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <./3-error_code.py> <url>")
        sys.exit(1)

    url = sys.argv[1]
    get_req(url)
