#!/usr/bin/python3
"""
MyInt Class Module.
"""


class MyInt(int):
    """
    Myint class is a subclass of int class.
    """

    def __init__(self, num):
        """
        The class constructor.
        """
        super().__init__()

    def __eq__(self, other):
        """
        Inverts the defualt value when comparing MyInt
        to an int object using '=='
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the defualt value when comparing MyInt
        to an int object using '!='
        """
        return super().__eq__(other)
