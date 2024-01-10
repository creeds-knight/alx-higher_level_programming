#!/usr/bin/python3
"""A module for pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns Pascal's triangle
    """
    if n <= 0:
        return []
    new_lst = []
    row = [1]
    for i in range(n):
        m = row[:] + [0]
        x1, x2 = 0, 1
        row = [1]
        for j in range(i):
            row.append(m[x1] + m[x2])
            x1 += 1
            x2 += 1
        new_lst.append(row)
    return new_lst
