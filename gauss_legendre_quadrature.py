#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

# функция
def f(x):
    return math.sqrt(1 + 2 * x)

# полином Лежандра Pn(x)
def pn(a, n, m, x):
    p = 0.0
    if m == 0:
        for i in range(0, n + 1, 2):
            if x == 0:
                break
            p += a[i] * pow(x, i)
    else:
        for i in range(1, n + 1, 2):
            p += a[i] * pow(x, i)
    return p

# производная Pn(x)
def dn(a, n, m, x):
    p = 0.0
    if m == 0:
        for i in range(0, n + 1, 2):
            if x == 0:
                break
            p += i * a[i] * pow(x, i - 1)
    else:
        for i in range(1, n + 1, 2):
            p += i * a[i] * pow(x, i - 1)
    return p

# факториал
def fact(n):
    f = 1.0
    for i in range(2, n + 1):
        f *= i
    return f

n = int(input('введите n для Pn(x):\n'))
c = float(input('введите нижний предел интегрирования:\n'))
d = float(input('введите верхний предел интегрирования:\n'))

if n <= 0:
    quit()

g = 0.0
m = n % 2
N = 0
a = [None] * (n + 1)

if m == 0:
    N = int(n / 2)
else:
    N = int((n - 1) / 2)

for i in range(N + 1):
    a[n - 2 * i] = (pow(-1, i) * fact(2 * n - 2 * i)) / (pow(2, n) * fact(i) * fact(n - i) * fact(n - 2 * i))

print('полином Лежандра:', end=' ')
if m == 0:
    output = str(a[0])
    for i in range(2, n + 1, 2):
        output += ' + (' + str(a[i]) + ')x^' + str(i)
    print(output)
else:
    output = '(' + str(a[1]) + ')x'
    for i in range(3, n + 1, 2):
        output += ' + (' + str(a[i]) + ')x^' + str(i)
    print(output)

# корни Pn(x)
y = [None] * (n + 1)
z = [None] * (n + 1)
w = [None] * (n + 1)
l = 0.0
s = 0.0
v = 0.0
for i in range(n):
    z[i] = math.cos(math.pi * (i + 0.75) / (n + 0.5))
    l = z[i]
    for j in range(1000):
        s = l - (pn(a, n, m, l) / dn(a, n, m, l))
        v = l
        l = s
    y[i] = l
    w[i] = 2 / ((1 - pow(l, 2)) * (dn(a, n, m, l) * dn(a, n, m, l)))

u = [None] * (n + 1)
for i in range(n):
    u[i] = ((d - c) * y[i] / 2) + (c + d) / 2

print('    корни      веса')
for i in range(n):
    print('{0:9f} {1:9f}'.format(y[i], w[i]))

for i in range(n):
    g += w[i] * f(u[i])

g *= (d - c) / 2
print('результат интегрирования = {0}'.format(g))
