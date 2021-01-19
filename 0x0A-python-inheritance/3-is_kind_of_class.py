#!/usr/bin/python3
"""Checks that a class is a subclass"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is a subclass of a given class.

    Args:
        obj(object): the object being tested
        a_class(class): the class being tested for"""
    return isinstance(obj, a_class)
