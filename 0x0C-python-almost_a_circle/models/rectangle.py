#!/usr/bin/python3
"""This is the rectangle shape"""
from models.base import Base


class Rectangle(Base):
    """This class inherits base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle.

        Args:
            width(int): width of the rectanlge
            height(int): height of the rectangle
            x(int): x location of the rectanlge
            y(int): y location of the rectangle
            id(int): id of the shape"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns the string rep of the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
    @property
    def width(self):
        """ int: width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of rectangle
        Args:
            value(int): value to set width to"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ int: height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle
        Args:
            value(int): value to set height to"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ int: x location of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x location of rectangle
        Args:
            value(int): value to set x to"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: y location of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y location of rectangle
        Args:
            value(int): value to set y to"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle"""
        pr = "\n" * self.y
        pr += (" " * self.x + "#" * self.width + "\n") * self.height
        print("{}".format(pr), end="")

    def update(self, *args, **kwargs):
        """Updates the rectangle
        Args:
            args(list): list of arguments
            kwargs(list): a list of dictoniary like arguements"""
        if len(args) > 0:
            if args[0]:
                self.id = args[0]
            if args[1]:
                self.width = args[1]
            if args[2]:
                self.height = args[2]
            if args[3]:
                self.x = args[3]
            if args[4]:
                self.y = args[4]
        else:
            if 'height' in kwargs:
                self.height = kwargs.get('height')
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'width' in kwargs:
                self.width = kwargs.get('width')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')
