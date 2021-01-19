#!/usr/bin/python3
""" This module creates a class that inherits the list class"""


class MyList(list):
    """Custom class that inherits list built-in"""
    def print_sorted(self):
        """Prints a sorted version of the inherited list"""
        print(sorted(self))
