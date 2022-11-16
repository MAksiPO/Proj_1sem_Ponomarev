##Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
##арифметическое элементов список с номерами от K до L включительно.

a = []

N = int(input("N:"))

for i in range(N):
   a.append(int(input("A: ")))

K = int(input("K:"))
L = int(input("L:"))

sum = 0
for i in range(0, K - 1):
   sum += a[i]
for i in range(L, N):
   sum += a[i]

print(sum)