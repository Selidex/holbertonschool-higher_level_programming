#!/usr/bin/python3
""" This module adds area and perimeter to the rectangle class"""


class Rectangle:
    """ This is a simple rectangle class.

    Attributes:
        number_of_instances(int): how many active rectangles exist
        print_symbol(any): the symbol called when printing
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle.

        Args:
            width(int): width of rectangle, defaults to 0
            height(int): height of rectangle, defaults to 0"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Returns a string representation of the class"""
        if self.__width is 0 or self.__height is 0:
            return ""
        else:
            s = "{}".format(self.print_symbol)
            s = ((s * self.width) + "\n") * self.height
            return s[:-1]

    def __repr__(self):
        """ Returns official string rep of the class"""
        return 'Rectangle(%s, %s)' % (self.width, self.height)

    def __del__(self):
        """ Deletion protocols"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of a rectangle."""
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the bigger rectangle.

        Args:
            rect_1(Rectangle): rectangle 1
            rect_2(Rectangle): rectangle 2
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
