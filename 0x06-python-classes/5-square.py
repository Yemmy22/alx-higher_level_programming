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
        self.size = size

    @property
    def size(self):
        ''' Returns the value of size '''
        return self.__size

    @size.setter
    def size(self, size):
        ''' Checks and sets the value of size as positive integer value.'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Returns the area of a square instance.'''
        return self.__size * self.__size

    def my_print(self):
        ''' Print to stdout a square with size represented by '#'. '''
        if self.__size == 0:
            print()
        i = j = 0
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
