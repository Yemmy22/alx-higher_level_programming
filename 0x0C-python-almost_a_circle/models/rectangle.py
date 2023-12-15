#!/usr/bin/python3
'''
A Rectangle class derived from Base class.
'''
from models.base import Base


class Rectangle(Base):
    @property
    def width(self):
        '''
        Return the value of private attribute width.
        '''
        return self.__width

    @width.setter
    def width(self):
        '''
        Sets the value of private attribute width.
        '''
        self.__width = width

    @property
    def height(self):
        '''
        Return the value of private attribute height.
        '''
        return self.__height

    @height.setter
    def height(self):
        '''
        Sets the value of private attribute height.
        '''
        self.__y = y
        self.__height = height

    @property
    def x(self):
        '''
        Return the value of private attribute x.
        '''
        return self.__x

    @x.setter
    def x(self):
        '''
        Sets the value of private attribute x.
        '''
        self.__y = y
        self.__x = x

    @property
    def y(self):
        '''
        Return the value of private attribute y.
        '''
        return self.__y

    @y.setter
    def y(self):
        '''
        Sets the value of private attribute y.
        '''
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initilaizes a rectangle.
        '''
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
