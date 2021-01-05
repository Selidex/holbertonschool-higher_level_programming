#!/usr/bin/python3
"""This module adds additional methods to the class
"""


class Square:
    """This class possesses additional methods
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

    def my_print(self):
        """This method prints the square.
        """
        if self.size is 0:
            print("")
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print("")
