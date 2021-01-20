#!/usr/bin/python3
"""This module turns an object into JSON"""


import json


def to_json_string(my_obj):
    """Convert object to json"""
    return json.dumps(my_obj)
