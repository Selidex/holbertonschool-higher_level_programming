#!/usr/bin/python3
"""This module is for Square classes"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class is a square subclass of Rectangle"""
    def __init__(self, size):
        """Initializes square.

        Args:
            size(int): width and height of the square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string rep of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """returns the area of the square"""
        return super().area()
