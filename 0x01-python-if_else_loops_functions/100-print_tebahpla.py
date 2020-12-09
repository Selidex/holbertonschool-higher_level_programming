#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 is 0:
        k = i
    else:
        k = i - 32
    print("{:c}".format(k), end="")
