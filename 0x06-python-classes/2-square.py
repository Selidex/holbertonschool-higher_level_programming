#!/usr/bin/python3
"""This module shows initial value validation.
"""


class Square:
    """This class shows value validation.
    """
    def __init__(self, size=0):
        """Square init.

        Args:
            size (int): the size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
