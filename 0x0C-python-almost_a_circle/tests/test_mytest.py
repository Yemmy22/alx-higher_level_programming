#!/usr/bin/python3
''' test_mytest and function module.'''


import unittest


def addition(num1, num2):
    '''Add two integers.'''
    return num1 + num2


def division(num1, num2):
    '''Return the integer division of two integers.'''
    return num1 / num2


def multiplication(num1, num2):
    '''Return the product of two integer multiplication.'''
    return num1 * num2


class test_mytests(unittest.TestCase):
    '''Subclass of unittest.TestCase.'''
    def test_addition(self):
        '''Class method tests addition.'''
        self.assertEqual(addition(5, 3), 8)

    def test_division(self):
        '''Class method tests division.'''
        self.assertEqual(division(21, 7), 3)

    def test_multiplication(self):
        '''Class method tests multiplication.'''
        self.assertEqual(multiplication(5, 3), 15)


if __name__ == '__main__':
    unittest.main()
