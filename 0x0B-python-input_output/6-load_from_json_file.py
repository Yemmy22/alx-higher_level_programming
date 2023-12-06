#!/usr/bin/python3
''' load_from_json_file function module.'''

import json


def load_from_json_file(filename):
    '''
    prints deserialized string object from json format in a file.
    '''
    with open(filename, 'r', encoding="utf-8") as file_name:
        obj = json.load(file_name)
        return obj
