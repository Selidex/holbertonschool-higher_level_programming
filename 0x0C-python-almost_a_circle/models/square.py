#!/usr/bin/python3
"""This module contains the Square class that inherits Rectanlge"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inits the square.
        Args:
            size(int): size of square
            x(int): x location
            y(int): y location
            id(int): id of square"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """ int: size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of the square.
        Args:
            value(int): size to set square to"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square
        Args:
            args(list): list of arguments
            kwargs(list): a list of dictoniary like arguements"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.size = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """Returns the dictionary definition of the class"""
        squ = {
            'id' : self.id,
            'x' : self.x,
            'y' : self.y,
            'size' : self.size
        }
        return squ
