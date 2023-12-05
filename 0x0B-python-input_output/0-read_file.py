#!/usr/bin/python3
'''Read_file function module.'''


def read_file(filename=""):
    '''Read and prints to to the screen the content of a file.'''
    with open(filename, encoding="utf-8") as file_name:
        print(file_name.read(), end='')
