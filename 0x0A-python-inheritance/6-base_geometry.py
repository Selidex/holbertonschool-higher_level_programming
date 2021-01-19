#!/usr/bin/python3
"""This module updates BaseGeometr to hold basic info"""


class BaseGeometry:
    """This version of BaseGeomety simply raises an exception"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
