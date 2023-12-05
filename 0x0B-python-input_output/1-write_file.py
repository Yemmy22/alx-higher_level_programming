#!/usr/bin/python3
''' write_file function module.'''


def write_file(filename="", text=""):
    '''
    writes a string into a file and returns
    number of characters written.
    '''
    with open(filename, 'w', encoding="utf-8") as file_name:
        chars_written = file_name.write(text)
        return chars_written

