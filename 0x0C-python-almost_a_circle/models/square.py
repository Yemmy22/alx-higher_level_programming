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
