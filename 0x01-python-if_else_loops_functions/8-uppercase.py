#!/usr/bin/python3
def uppercase(str):
    s = []
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        s = i
        print('{}'.format(s), end='')
    print()
