#!/usr/bin/python3
'''
A Rectangle class module.
'''
from models.base import Base


class Rectangle(Base):
    '''
    A rectangle class inheriting Base Class.
    '''
    @property
    def width(self):
        '''
        Return the value of private attribute width.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Sets the value of private attribute width.
        '''
        self.__width = value

    @property
    def height(self):
        '''
        Return the value of private attribute height.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Sets the value of private attribute height.
        '''
        self.__height = value

    @property
    def x(self):
        '''
        Return the value of private attribute x.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Sets the value of private attribute x.
        '''
        self.__x = value

    @property
    def y(self):
        '''
        Return the value of private attribute y.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Sets the value of private attribute y.
        '''
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initilaizes a rectangle.
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
