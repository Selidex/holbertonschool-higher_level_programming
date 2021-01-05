#!/usr/bin/python3
"""This module demonstrates the __init__ method
when making classes
"""


class Square:
    """This class shows the init method.
    """
    def __init__(self, val):
        """Square initializing method.

        Args:
            val (int): the size of the square
        """
        self.__size = val
