#!/usr/bin/python3
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
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the json string to a file"""
        filename = cls.__name__ + ".json"
        jlist = list([])
        for x in list_objs:
            jlist.append(Base.to_json_string(x.to_dictionary()))
        with open(filename, 'w') as fin:
            fin.write(str(jlist))
