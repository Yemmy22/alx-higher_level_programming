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
    def size(self, size):
        ''' Checks and sets the value of size as positive integer value.'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError('position must be a tuple of 2 positive\
 integers')
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        '''Returns the area of a square instance.'''
        return self.__size * self.__size

    def my_print(self):
        ''' Print to stdout a square with size represented by '#'. '''
        if self.__size == 0:
            print()
        i = j = 0
        for i in range(self.__size):
            if self.__position[1] > 0:
                print(self.__position[0] * "_", end='')
            else:
                print(self.__position[0] * " ", end='')
            for j in range(self.__size):
                print('#', end='')
            print()
