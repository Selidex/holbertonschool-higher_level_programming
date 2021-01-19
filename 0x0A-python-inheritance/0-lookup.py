#!/usr/bin/python3
""" This module looks up the properties of an object"""


def lookup(obj):
    """ This function looks up the attributes of an object.

    Args:
        obj(object): object being looked up"""
    return dir(obj)
