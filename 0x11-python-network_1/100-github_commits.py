#!/usr/bin/python3

"""Make requests using the requests module"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
                                                                sys.argv[1],
                                                                sys.argv[2]))
    count = 0
    for commit in r.json():
        if count > 9:
            break
        print("{}: {}".format(
                        commit.get("sha"),
                        commit.get("commit").get("committer").get("name")))
        count += 1
