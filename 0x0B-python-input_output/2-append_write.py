#!/usr/bin/python3
"""This module appends a file"""


def append_write(filename="", text=""):
    """APpend to a file"""
    with open(filename, 'a') as fin:
        fin.write(text)
    return len(text)
