#!/usr/bin/python3

"""Make requests using the requests module"""

import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("    - type:", type(r.text))
    print("    - content:", r.text)
