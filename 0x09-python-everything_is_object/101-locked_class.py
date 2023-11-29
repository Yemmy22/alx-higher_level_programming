#!/usr/bin/python3
'''A Locked Class.'''


class LockedClass:
    ''' Prevent any attribute other than "first_name"
    to be created by an insrance.'''
    __slots__ = ("first_name",)
