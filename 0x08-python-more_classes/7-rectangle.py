#!/usr/bin/python3

''' A rectangle class module. '''


class Rectangle:
    '''Defines rectangle class.'''

    number_of_instances = 0  # Class field for number of instances
    print_symbol = "#"  # Class field for symbols

    def __init__(self, width=0, height=0, print_symbol='#'):
        '''
        Initialize rectangle instances with attribute
        priavte attribute 'width' and 'height'.
        '''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        self.print_symbol = print_symbol

    def __str__(self):
        '''
        Returns an empty string if either 'width' or 'height' is
        0, or return a '#' string representing the
        aforementioned attributes.
        '''

        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)
            result += '\n'
        return result[:-1]

    def __repr__(self):
        '''
        Returns a string representation of rectangle
        that can recreate a new instance using eval()
        '''
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"

    def __del__(self):
        '''
        Prints a string when a rectangle deleted
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        '''
        Return the value of private instance attribute
        'width'.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Sets the value of  private instance attribute
        'width' to a positive integer.
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Return the value of private instance attribute
        'height'.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Sets the value of private instance
        attribute 'height' to a positive integer.
        '''
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def print_symbol(self):
        '''
        Gets the value of print_symbol.
        '''
        return self.__print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        '''
        Sets the value of print_symbol.
        '''
        self.__print_symbol = value

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
