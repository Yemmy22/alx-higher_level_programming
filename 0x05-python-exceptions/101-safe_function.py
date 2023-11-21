#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except ZeroDivisionError as zd:
        print("Exception: {}".format(*zd.args), file=sys.stderr)
        return None
    except IndexError as ie:
        print("Exception: {}".format(*ie.args), file=sys.stderr)
        return None
    return result
