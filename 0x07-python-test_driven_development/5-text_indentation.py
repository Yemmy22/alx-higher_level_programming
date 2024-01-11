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
    for i in text:
        print('{}'.format(i), end='')
        for j in delimeter:
            if i == j:
                print('\n')
