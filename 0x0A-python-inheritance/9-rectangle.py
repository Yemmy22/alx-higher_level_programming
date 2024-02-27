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
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        elif value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    '''
    A BaseGeometry subclass with width and height attributes.
    '''
    def __init__(self, width, height):
        ''' Initializes Rectangle objects.'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Returns the area of a rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Returns a user friendly representation of a rectangle
        '''
        return "[{}] {}/{}".\
            format(self.__class__.__name__, self.__width, self.__height)
