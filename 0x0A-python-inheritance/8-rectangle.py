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
        self.name = name
        if type(value) != int:
            raise TypeError(self.name + ' must be an integer')
        elif value <= 0:
            raise ValueError(self.name + ' must be greater than 0')
        else:
            self.value = value


class Rectangle(BaseGeometry):
    '''
    A BaseGeometry subclass with width and height attributes.
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
