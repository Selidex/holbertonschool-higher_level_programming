#!/usr/bin/python3
"""This module splits a string into mulitple lines
"""


def text_indentation(text):
    """This function splits a string

    Arg:
        text(string): the string to be split
    """
    b = 0
    c = 1
    arr = [".", ":", "?"]
    if type(text) != str:
        raise TypeError("text must be a string")
    for x in text:
        if b is 1:
            print("")
            print("")
            b = 0
            c = 1
        if x in arr:
            b = 1
        if x is " " and c is 1:
            continue
        else:
            c = 0
            print("{}".format(x), end="")
