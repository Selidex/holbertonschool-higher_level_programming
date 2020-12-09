#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            k = chr(ord(i) - 32)
        else:
            k = i
        print("{}".format(k), end="")
    print("")
