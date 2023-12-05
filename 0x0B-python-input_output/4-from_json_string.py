#!/usr/bin/python3
'''from_json_string function module.'''


import json


def from_json_string(my_str):
    '''Returns string object from deserialized json format.'''
    return json.loads(my_str)
