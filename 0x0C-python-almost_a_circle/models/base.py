#!/usr/bin/python3
'''
A Base class module.
'''
import json


class Base:
    '''
    Base class.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Base class constrructor.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns a serialized json string of a rectangle's dict
        representation if the list is not None or empty.
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
