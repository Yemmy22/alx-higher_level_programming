#!/usr/bin/python3
'''
matrix_divided function module.
matrix: a list of lists of integers
div: integer divisor
'''


def matrix_divided(matrix, div):
    '''
    Returns a a new matrix with divided of previous sub elements sub-elements.
    '''
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    i = j = 0
    new_list = []
    for i in range(len(matrix)):
        sub_list = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError('matrix must be a\
 matrix (list of lists) of integers/floats')
            sub_list.append(round(matrix[i][j]/div, 2))
        if i == 0:
            first_row = j
        else:
            other_row = j
        if i >= 1:
            if first_row != other_row:
                raise TypeError('Each row of the\
 matrix must have the same size')
        new_list.append(sub_list)
    return new_list
