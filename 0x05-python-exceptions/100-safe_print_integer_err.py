#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", end=' ', file=sys.stderr)
        for i in ex.args:
            print(i, file=sys.stderr)
            '''single line alternative for entire exception block:
                print("Exception: {}".format(*ex.args), file=sys.stderr)'''
            return False
    return True
