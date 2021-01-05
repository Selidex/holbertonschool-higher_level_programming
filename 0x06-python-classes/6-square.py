#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        te = "position must be a tuple of 2 positive integers"
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if not isinstance(i, int):
                raise TypeError(te)
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
            return
        if value < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        te = "position must be a tuple of 2 positive integers"
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int):
                raise TypeError(te)
        self.__position = position

    def my_print(self):
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
