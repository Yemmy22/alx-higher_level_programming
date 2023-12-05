#!/usr/bin/python3
'''
inherits_from function module.
'''


def inherits_from(obj, a_class):
    '''
    Return true is instance is an object of subclass
    of a_class or false if otherwise.
    '''
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
