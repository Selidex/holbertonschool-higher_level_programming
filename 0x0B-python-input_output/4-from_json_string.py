#!/usr/bin/python3
"""Converts a json to an object"""


import json


def from_json_string(my_str):
    """Convert json to object"""
    return json.loads(my_str)
