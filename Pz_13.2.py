import random
N=int(input("Введите размер матрицы:"))
arr=[[random.randint(1,9) for i in range(N)] for j in range(N)]
min = arr[0][0]
max = 0
for i in range(N):
for j in range(N):
if(arr[i][j]<min):
min=arr[i][j]
elif(arr[i][j]>max):
max=arr[i][j]
for i in range(N):
print(arr[i])
print(max, min)