#!/usr/bin/python3
'''
An empty Square Class Module.
'''


class Square:
    '''
    A Class representing a Square.
    '''
    def __init__(self, size):
        '''
        The init class method initializes any instance of Square
        with private attribute 'size'.

        Parameters:
            size (int): The size of the square.
        '''
        self.__size = size
