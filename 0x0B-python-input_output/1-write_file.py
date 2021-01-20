#!/usr/bin/python3
"""This module writes to a file"""


def write_file(filename="", text=""):
    """writes a file"""
    with open(filename, 'w') as fin:
        fin.write(text)
    return len(text)
