#!/usr/bin/python3
def matrix_divided(matrix, div):

    try:
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        if not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        m = len(matrix[0])

        new_matrix = []

        for i in matrix:
            new_row = []
            if not isinstance(i, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(i) != m:
                raise TypeError("Each row of the matrix must have the same size")
            for j in i:
                if type(j) not in (int,float):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

                n = round(j/div, 2)
                new_row.append(n)
            new_matrix.append(new_row)
        return new_matrix
    except NameError:
         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

