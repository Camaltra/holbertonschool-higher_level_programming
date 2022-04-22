#!/usr/bin/python3

"""Fetching data from URL"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()

    print("Body response:")
    print("    - type:", type(body))
    print("    - content:", body)
    print("    - utf8 content:", body.decode("utf-8"))
