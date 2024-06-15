#!/usr/bin/python3
""" computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_lst = []
    for elm in matrix:
        new = []
        for num in elm:
            n = num ** 2
            new.append(n)
        new_lst.append(new)

    return new_lst
