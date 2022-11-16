##Дан массив размера N, все элементы которого, кроме одного, упорядочены по убыванию. Сделать массив упорядоченным, переместив элемент, нарушающий упорядоченность, на новую позицию.
import random
N = random.randrange(1,21)
##N = 1
##N = 15
a = [random.randrange(1,210) for i in range(N)]
a.sort()
K = random.randrange(0,N)
x = random.randrange(a[K],210)
a = a[:K] + [x] + a[K:]
##a = [7, 8, 20, 22, 30, 55, 79, 88, 116, 150, 161, 173, 179, 174, 197, 209]
##a = [6, 29, 39, 77, 80, 88, 201, 126, 145, 168, 173, 180, 193]
N = len(a)
print("N = ", N)
print("Array:\n",a)
K = 1
while K < N-1 and a[K-1] <= a[K] and a[K] <= a[K+1] :
    K += 1
print("K:",K)
x = a[K]
print("x:",x)
print("move")
while K < N-1 and x > a[K+1] :
    a[K] = a[K+1]
    K += 1
a[K] = x
print("Modified Array:\n",a)