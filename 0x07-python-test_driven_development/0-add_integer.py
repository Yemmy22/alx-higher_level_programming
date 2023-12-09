#!/usr/bin/python3
'''
add_ineteger function module.
a: first argument
b: first argument
'''


def add_integer(a, b=98):
    '''
    Returns the integer sum of two numbers.
    '''
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
