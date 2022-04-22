#!/usr/bin/python3

import requests

r = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print("    - type: ", type(r))
print("    - content: ", r)