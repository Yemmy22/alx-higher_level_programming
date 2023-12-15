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
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
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
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self, value):
        '''
        Return the value of private attribute x.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Sets the value of private attribute x.
        '''
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
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
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initilaizes a rectangle.
        '''
        super().__init__(id)
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def __str__(self):
        '''
        Returns an unofficial string representation.
        '''
        return "[Rectangle] " + "(" + str(self.id) + ") "\
            + str(self.__x) + '/' + str(self.__y) + ' - ' +\
            str(self.__width) + '/' + str(self.__height)

    def area(self):
        '''
        Return the product of a rectangle's width and height.
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Displays the width and height of a rectangle,
        represented by '#'.
        '''
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()
