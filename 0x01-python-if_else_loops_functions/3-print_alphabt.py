#!/usr/bin/python3
for i in range(97, 123):
    if (i != 101 | i != 113):
        print("{:c}".format(i), end="")
