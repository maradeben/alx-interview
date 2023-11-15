#!/usr/bin/python3
""" rotate a 2d square matrix 90 degrees """


def rotate_2d_matrix(matrix):
    """ rotate the 2d matrix in place, do not return anything """
    
    if type(matrix) != list or len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    size = len((matrix))
    new = [[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            new[j][i] = matrix[i][j]

    for i in range(size):
        matrix[i] = new[i]
