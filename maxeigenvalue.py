#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
from numpy import linalg
from matrix_input import matrix_input

def max_eigenvalue(matrix):
    eigenvalues, _ = linalg.eig(numpy.array(matrix, numpy.float64))
    return max(eigenvalues)

matrix, n = matrix_input()

max = max_eigenvalue(matrix)

print('матрица:\n{0}\n\nмаксимальное собственное число: {1}'.format(matrix, max))
