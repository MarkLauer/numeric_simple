#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from matrix_input import matrix_input

matrix, n = matrix_input()

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            quit('матрица не симметрична')

print('введите вектор b:')
vector = [int(input()) for i in range(n)]

u = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    temp = 0
    for k in range(i):
        temp += u[k][i] * u[k][i]
    u[i][i] = math.sqrt(matrix[i][i] - temp)
    for j in range(i, n):
        temp = 0
        for k in range(i):
            temp += u[k][i] * u[k][j]
        u[i][j] = (matrix[i][j] - temp) / u[i][i]

y = [0 for i in range(n)]
for i in range(n):
    temp = 0
    for k in range(i):
        temp += u[k][i] * y[k]
    y[i] = (vector[i] - temp) / u[i][i]

x = [0 for i in range(n)]
for i in range(n - 1, 0, -1):
    temp = 0
    for k in range(i + 1, n):
        temp += u[i][k] * x[k]
    x[i] = (y[i] - temp) / u[i][i]

print(x)
