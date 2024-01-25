#!/usr/bin/python3
'''
A Square class Module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A subclass of Rectangle class inherinting all Rectangle attributes
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        A class constructor that initializes the Square object
        with the atributes of a Rectangle.
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''
        Formats the string representation of a Square object.
        '''
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        '''
        Gets the value of size as the value of width
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Sets te value of size to both width and height
        '''
        self.width = value
        self.height = value
