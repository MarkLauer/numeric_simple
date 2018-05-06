#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
from numpy import linalg
from matrix_input import matrix_input

def danilevsky(matrix):
    eigenvalues, eigenvectors = linalg.eig(numpy.array(matrix, numpy.float64))
    return eigenvalues.tolist(), eigenvectors.tolist()

matrix, n = matrix_input()

eigenvalues, eigenvectors = danilevsky(matrix)

print('матрица:\n{0}\n\nсобственные числа: {1}\nсобственные векторы:\n{2}'.format(matrix, max, eigenvalues, eigenvectors))
