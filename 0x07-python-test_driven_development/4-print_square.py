#!/usr/bin/python3
""" This module is a simple print function meant to help
develope simple test case files"""


def print_square(size):
    """This function prints a square

    Arg:
        size(int): the size of the program
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for x in range(0, size):
        print("#" * size)
