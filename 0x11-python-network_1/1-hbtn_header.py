#!/usr/bin/python3

"""Fetching specific header value from URL"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info().get('X-Request-Id'))
