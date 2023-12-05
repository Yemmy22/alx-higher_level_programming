#!/usr/bin/python3
''' Class MyList Module'''


class MyList(list):
    ''' Defines MyList Class as a subclass of in-built Class list.'''

    def __init__(self):
        ''' Initializes objects of MyList.'''
        list.__init__(self)

    def print_sorted(self):
        ''' Print instances of MyList in a sorted order.'''
        print(sorted(self))
