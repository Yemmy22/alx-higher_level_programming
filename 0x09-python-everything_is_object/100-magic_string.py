#!/usr/bin/python3
def magic_string():
    magic_string.itr = getattr(magic_string, 'itr', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.itr - 1)
