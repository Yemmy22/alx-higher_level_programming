#!/usr/bin/python3

''' A rectangle class module. '''


class Rectangle:
    '''Defines rectangle class.'''

    def __init__(self, width=0, height=0):
        '''Initialize rectangle instances with attribute\
 priavte attribute 'width' and 'height'.'''
        self.height = height
        self.width = width

    def __str__(self):
        '''
        Returns an empty string if either 'width' or 'height' is
        0, or  returns a '#' string representing the
        aforementioned attributes.
        '''
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += '\n'
        return result

    @property
    def width(self):
        '''Return the value of private instance attribute 'width'.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the value of  private instance attribute\
 'width' to a positive integer.'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Return the value of private instance attribute 'height'.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the value of private instance\
 attribute 'height' to a positive integer.'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''
        Return the area of a rectangle.
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        Return the perimeter of a rectangle.
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
