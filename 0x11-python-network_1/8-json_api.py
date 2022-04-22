#!/usr/bin/python3

"""Make requests using the requests module"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv <= 1):
        q = ""
    else:
        q = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        responseDict = r.json()
        name = responseDict.get("name")
        id = responseDict.get("id")
        if id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except TypeError:
        print("Not a valid JSON")
