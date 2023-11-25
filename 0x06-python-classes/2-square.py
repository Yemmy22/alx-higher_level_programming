#!/usr/bin/python3
'''
An empty Square Class Module.
'''


class Square:
    '''
    A Class representing a Square.
    '''
    def __init__(self, size=0):
        '''
        The init class method initializes any instance of Square
        with private attribute 'size' which must be a
        positive integer.

        Parameters:
            size: The size input of the square.
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
