#!/usr/bin/python
# -*- coding: utf-8 -*-

def matrix_input():
    n = int(input('введите размерность матрицы: '))
    print('введите матрицу:')
    matrix = [[int(input()) for i in range(n)] for j in range(n)]
    return matrix, n
