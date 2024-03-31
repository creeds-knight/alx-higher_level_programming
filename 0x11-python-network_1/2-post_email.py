#!/usr/bin/python3
""" post a request to the passed url with email parameter and displays body
    of the response
"""
import sys
import urllib.request
import urllib.parse
import urllib.error


def email_post(url, email):
    """ A function to post an email"""
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print("HTTP Error code: ", e.code)
    except urlib.error.URLError as e:
        print("URL Error:", e.reason)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    email_post(url, email)
