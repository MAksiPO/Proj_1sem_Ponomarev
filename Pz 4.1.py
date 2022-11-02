#Пз4.1 Дано вещественное число X и целое число N (> 0). Найти значение выражения 1 - X 2 /(2!) + X4 /(4!) - ... + (-1)N -X 2*N/((2-N)!) (N! = 12 ...N). Полученное число является приближенным значением функции cos в точке X.

import math
X = 2
N = 20
print('X = ', X)
print('N = ', N)
F = 1.0
S = 1.0
for i in range(1,N+1):
    F *= X / i
    S += F
    print(i," : ", F," : ", S)
print("Result:")
print(S)
print("e:")
print(math.exp(X))