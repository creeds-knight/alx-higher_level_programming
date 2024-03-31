#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using urllib package"""
if __name__ == "__main__":
    import urllib.request


    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- type: {}".format(html))
    print("\t- type: {}".format(html.decode('utf-8')))




