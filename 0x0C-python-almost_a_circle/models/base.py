B#!/usr/bin/python3
"""This module is the base class of all shapes in this project"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Sends the dictionary to a json string"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a json string to a dictionary"""
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the json string to a file"""
        filename = cls.__name__ + ".json"
        jlist = []
        if list_objs is not None:
            for x in list_objs:
                jlist.append(cls.to_dictionary(x))
        with open(filename, 'w') as fin:
            fin.write(cls.to_json_string(jlist))

    @classmethod
    def create(cls, **dictionary):
        """This method creates a new shape using a dictionary"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This method creates a new shape from a file"""
        filename = cls.__name__ + ".json"
        jlist = []
        try:
            with open(filename, mode="r") as fin:
                jlist = cls.from_json_string(fin.read())
            for x in jlist:
                jlist[x] = cls.create(**jlist[x])
        except:
            return []
        return jlist
