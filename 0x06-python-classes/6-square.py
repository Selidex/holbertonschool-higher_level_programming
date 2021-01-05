#!/usr/bin/python3
"""This module adds a new parameter to be updated
"""


class Square:
    """This class is a square that also contains a position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Square initializer

        Args:
            size(int): size of the Square
            position(tuple): starting location of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        te = "position must be a tuple of 2 positive integers"
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError(te)
        j = 0
        for i in position:
            if not isinstance(i, int):
                raise TypeError(te)
            if position[j] < 0:
                raise TypeError(te)
            j += 1
        self.__position = position

    def area(self):
        """Returns the area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """int: size of square
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

    @property
    def position(self):
        """tuple:position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter methods

        Args:
            value(tuple): new position
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError(te)
        j = 0
        for i in value:
            if not isinstance(i, int):
                raise TypeError(te)
            if value[j] < 0:
                raise TypeError(te)
            j += 1
        self.__position = value

    def my_print(self):
        """This method prints the square.
        """
        if self.size is 0:
            print("")

        for i in range(0, self.position[1]):
            print("")
        for i in range(0, self.size):
            for x in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.size):
                print("#", end="")
            print("")
