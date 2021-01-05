#!/usr/bin/python3
"""This module shows none init methods with classes.
"""


class Square:
    """This square class has additional, non init, methods.
    """
    def __init__(self, size=0):
        """Square initializer

        Args:
            size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of the square
        """
        return (self.__size * self.__size)
