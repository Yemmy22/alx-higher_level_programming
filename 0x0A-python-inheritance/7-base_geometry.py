#!/usr/bin/python3
'''
BaseGeometry Class Module.
'''


class BaseGeometry:
    '''Define BaseGeometry Class.'''
    def area(self):
        ''' Raises exception when invoked.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Checks value is an integer greater than zero or raises
        exception if otherwise.
        '''
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        elif value <= 0:
            raise ValueError(name + ' must be greater than 0')
