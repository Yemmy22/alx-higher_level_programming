#!/usr/bin/python3
'''
is_kind_of_class function Module.
'''


def is_kind_of_class(obj, a_class):
    '''
    Return true, if obj  is an instance of a_class or its
    derived class or, false if otherwise.'''
    return isinstance(obj, a_class)
