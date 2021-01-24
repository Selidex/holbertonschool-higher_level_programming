#!/usr/bin/python3
"""This module is the base class of all shapes in this project"""


class Base:
    """This class forms the base of all shape classes"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initializes the class

        Args:
            id(int): shape id, defaults to nb if None"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
