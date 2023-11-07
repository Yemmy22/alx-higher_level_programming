#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            de_lm = ""
            if j < i[-1]:
                de_lm = " "
            print("{:d}".format(j), end=de_lm)
        print()
