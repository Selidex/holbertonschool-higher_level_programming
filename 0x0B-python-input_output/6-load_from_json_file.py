#!/usr/bin/python3
"""Takes a json file and turns it into an object"""


import json


def load_from_json_file(filename):
    """insert module documentation here as well"""
    with open(filename, 'r') as fin:
        return json.loads(fin.read())
