#!/usr/bin/python3
""" This module is a simple print function meant to help
develope simple test case files"""


def say_my_name(first_name, last_name=""):
    """This function prints a simple sentence.

    Arg:
        first_name(string): first name
        last_name(string): last name, defaults to ""
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
