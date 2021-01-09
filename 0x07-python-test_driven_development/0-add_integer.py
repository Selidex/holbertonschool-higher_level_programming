#!/usr/bin/python3
""" This module is a simple add interger function meant to learn how to
develope simple test case files"""


def add_integer(a, b=98):
    """Simple addition function

    Args:
        a (int): the first number
        b (int): the second number, defaults to 98
    """
    if not int(a) or float(a):
        raise TypeError("a must be an integer")
    if not int(b) or float(b):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
