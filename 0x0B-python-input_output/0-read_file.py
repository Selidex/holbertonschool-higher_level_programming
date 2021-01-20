#!/usr/bin/python3
"""THis module reads a file and prints to standard output"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, 'r') as fin:
        print(fin.read(), end="")
