#!/usr/bin/python3
'''append_write function module.'''


def append_write(filename="", text=""):
    '''
    Append string to the end of a file
    and return number of character written.
    '''
    with open(filename, 'a', encoding="utf-8") as file_name:
        chars_written = file_name.write(text)
        return chars_written
