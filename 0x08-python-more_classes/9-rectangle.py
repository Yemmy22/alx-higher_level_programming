#!/usr/bin/python3

''' A rectangle class module. '''


class Rectangle:
    '''Defines rectangle class.'''

    number_of_instances = 0  # Class field for number of instances
    print_symbol = "#"  # Class field for symbols

    def __init__(self, width=0, height=0):
        '''
        Initialize rectangle instances with attribute
        priavte attribute 'width' and 'height'.
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        The function returns the largest rectangle based on the area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        '''
        Returns a new Rectangle instance with width == height == size
        '''
        return cls(size, size)
