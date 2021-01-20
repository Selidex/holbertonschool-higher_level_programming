#!/usr/bin/python3
"""Checks specifically if a class is a subclass"""


def inherits_from(obj, a_class):
    """Checks if obj is a subclass of a_class

    Args:
        obj(object): the object being tested
        a_class(class): the class being tested for"""
    return isinstance(obj, a_class) and type(obj) is not a_class
