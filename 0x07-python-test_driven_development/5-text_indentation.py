#!/usr/bin/python3
'''
This is the text_indentation function module
'''


def text_indentation(text):
    '''
    The function prints two new lines after specified delimiters
    '''
    if type(text) != str:
        raise TypeError('text must be a string')
    delimeter = ['.', '?', ':']
    prev = None
    for i in text:
        if prev in delimeter and i == ' ':
            continue
        print('{}'.format(i), end='')
        for j in delimeter:
            prev = i
            if i == j:
                print('\n')
