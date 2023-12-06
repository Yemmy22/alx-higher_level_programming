#!/usr/bin/python3
'''add_item function module.'''


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    '''
    Write in a new file, serialized json format list
    of command line argument and appends successive argument
    list to the file.
    '''
    if not os.path.exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    list_obj = load_from_json_file("add_item.json")
    list_obj.extend(sys.argv[1:])
    save_to_json_file(list_obj, "add_item.json")


if __name__ == '__main__':
    add_item()
