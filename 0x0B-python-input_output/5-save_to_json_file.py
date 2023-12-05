#!/usr/bin/python3
'''save_to_json_file function module.'''

import json


def save_to_json_file(my_obj, filename):
    '''
    writes serialized string object in json format to a file.
    '''
    with open(filename, 'w', encoding="utf-8") as file_name:
        json.dump(my_obj, file_name)
