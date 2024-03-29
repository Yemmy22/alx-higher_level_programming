#!/usr/bin/python3
'''
A Base class module.
'''
import json
import sys
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes to file, in json format, dictionary
        representation of base subclasses.
        '''

        if list_objs is None:
            filename = "{}.json".format(cls.__name__, end='')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("[]")
        else:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            json_dict_list = cls.to_json_string(dict_list)

            filename = "{}.json".format(cls.__name__, end='')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(json_dict_list)

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns an object of base subclasses,
        from a deserialized json string.
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instantiated object of the subclasses of the
        base class with updated attributes.
        '''
        if cls.__name__ == "Square":
            obj = cls(1)
        else:
            obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''
        Reads a json format string from a file, deserialises the
        string to a python dict and uses the data to
        instantiate subclassess of the base class.
        '''
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        if not os.path.exists(filename):
            return instance_list
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()

        obj_list = cls.from_json_string(json_str)
        for obj in obj_list:
            instance_list.append(cls.create(**obj))
        return instance_list
