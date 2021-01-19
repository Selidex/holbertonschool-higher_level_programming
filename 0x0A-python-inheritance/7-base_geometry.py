#!/usr/bin/python3
"""This module updates BaseGeometr to hold basic info"""


class BaseGeometry:
    """This version of BaseGeomety add a value validator"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates that value is an integer"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
