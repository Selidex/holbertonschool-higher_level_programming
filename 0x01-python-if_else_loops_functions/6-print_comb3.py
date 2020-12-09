#!/usr/bin/python3
t = -1
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            if i is 8 and j is 9:
                print("89")
            else:
                print("{}{}, ".format(i, j), end="")
