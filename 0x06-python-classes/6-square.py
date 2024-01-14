#!/usr/bin/python3
'''
An empty Square Class Module.
'''


class Square:
    '''
    A Class representing a Square.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        The init class method initializes any instance of Square
        with private attribute 'size' which must be a
        positive integer.

        Parameters:
            size: The size input of the square.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' Returns the value of size '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Checks and sets the value of size as positive integer value.'''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if (type(value[0]) is int and value[0] >= 0)\
                    and (type(value[1]) is int and value[1] >= 0):
                self.__position = value
            else:
                raise TypeError('position must be a tuple of\
 2 positive integers')
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        '''Returns the area of a square instance.'''
        return self.__size * self.__size

    def my_print(self):
        '''
        Print to stdout a square with size represented by "#".
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
