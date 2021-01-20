#!/usr/bin/python3
"""This module contains a rectangle class inheriting from
Base Geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""
    def __init__(self, width, height):
        """Initializes rectangle

        Args:
            width(int): width of rectangle
            height(int): height of rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns the string representation of the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height
