#!/usr/bin/python3
"""This module shows the creation of properties
"""


class Square:
    """This class shows property methods
    """
    def __init__(self, size=0):
        """The init methods

        Args:
            size(int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method returnsthe area of hte square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """int: this is the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method

        Args:
            value(int): the size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
            return
        if value < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = value
