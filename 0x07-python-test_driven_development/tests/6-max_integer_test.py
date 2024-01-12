#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    Subclass of Unittest.Testcase Class
    '''
    max_integer_1 = (max_integer([1, 2, 3, 4]))
    max_integer_2 = (max_integer([1, 3, 4, 2]))
    max_integer_3 = (max_integer([10, 3, 6, 4]))
    max_integer_4 = (max_integer([35, 70, -100, 32]))
    max_integer_5 = (max_integer([-35, -70, -100, -32]))
    max_integer_6 = (max_integer([3]))
    max_integer_7 = (max_integer([]))

    def test_max_integer(self):
        '''
        Tests if the second positional arguement is the maximum integre
        '''
        self.assertEqual(self.max_integer_1, 4)
        self.assertEqual(self.max_integer_2, 4)
        self.assertEqual(self.max_integer_3, 10)
        self.assertEqual(self.max_integer_4, 70)
        self.assertEqual(self.max_integer_5, -32)
        self.assertEqual(self.max_integer_6, 3)
        self.assertEqual(self.max_integer_7, None)

    def test_exception_max_integer(self):
        '''
        Test that the max_integer raises an exception
        '''
        with self.assertRaises(TypeError):
            max_integer([35, 70, "white", 32])
