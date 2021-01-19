#!/usr/bin/python3
""" THis module checks if a class is exactly a class"""


def is_same_class(obj, a_class):
    """ checks if an object is a class.

    Args:
        obj(object): the object being tested
        a_class(class): the class """
    return type(obj) is a_class
