#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
from numpy import linalg
from matrix_input import matrix_input

# matrix, n = matrix_input()
#
# print('введите вектор b:')
# vector = [int(input()) for i in range(n)]

matrix = [[1, 3, -2, 0, -2], [3, 4, -5, 1, -3], [-2, -5, 3, -2, 2], [0, 1, -2, 5, 3], [-2, -3, 2, 3, 4]]
vector = [0.5, 5.4, 5.0, 7.5, 3.3]

print('матрица:\n{0}\n\nвектор: {1}\n'.format(matrix, vector))

x = linalg.solve(matrix, vector)

print('корни: {0}'.format(x))
