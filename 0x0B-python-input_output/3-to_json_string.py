#!/usr/bin/python3
'''to_json_string function module.'''


import json


def to_json_string(my_obj):
    '''Returns serialized json format of an object.'''
    return json.dumps(my_obj)
