#!/usr/bin/python3
""" Lookup function Module. """


def lookup(obj):
    ''' Returns a list of attributes and methods of the input
    object.'''
    return dir(obj)
