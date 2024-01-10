#!/usr/bin/python3
'''
This is the print_square module.
'''


def print_square(size):
    '''
    Prints a square with the character #
    Size: The lenght of the square
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for lenght in range(size):
            print('#' * size)
