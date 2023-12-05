#!/usr/bin/python3
''' is_same_class function Module.'''


def is_same_class(obj, a_class):
    '''
    Return true if instance is of type class or
    false if otherwise.
    '''
    if type(obj) == a_class:
        return True
    return False
