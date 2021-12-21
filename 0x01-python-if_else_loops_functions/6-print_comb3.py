#!/usr/bin/python3
for i in range(0, 10):
    j = i + 1
    while j < 10:
        if i == 8:
            print("89")
        else:
            print("{}{}".format(i, j), end=", ")
        j += 1
