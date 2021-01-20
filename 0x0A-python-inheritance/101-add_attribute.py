#!/usr/bin/python3
"""Attempts to add an attribute to an object"""


def add_attribute(obj, name, value):
    """Attempts to add an attribute to an object if possible"""
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
