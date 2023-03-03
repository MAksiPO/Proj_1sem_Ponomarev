# В матрице найти сумму элементов первых двух строк.
from random import randint

x = int(input('Введите количество столбцов: '))
y = int(input('Введите количество строк: '))
A = [[randint(0, 10) for i in range(x)] for j in range(y)]

for i in range(len(A)): # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])): # len(A[i]) - возвращает количество элементов в строке i
        print(A[i][j], end=' ')
    print()

print('Сумма элементов первых двух строк:', sum(A[0])+sum(A[1]))