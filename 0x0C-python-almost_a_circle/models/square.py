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

    def update(self, *args, **kwargs):
        '''
        Modifies the value of a square's attributes.
        '''
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
