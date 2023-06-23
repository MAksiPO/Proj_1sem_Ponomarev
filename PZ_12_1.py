import random

n = int(input("Введите число элементов массива: "))

lst = [random.randint(-100,100) for x in range(n)]
print(f"Список элементов массива: {lst}")

lst1 = len([x for x in lst[:n//2] if x > 0])
print(f'Количество положительных элементов в первой половине: {lst1}')