# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трем:
# Количество чисел кратных трем:

import random


def sequence(n) -> str:  # создаем функцию генерации последовательности
    line_sequence = []  # Объявляем пустой список
    while n != 0:
        line_sequence.append(str(random.randint(-100, 100)))
        n -= 1
    line_sequence = " ".join(line_sequence)  # Записываем в строку список
    return line_sequence  # Возвращаем строку с последовательностью


file1 = open('file_data.txt', 'w+', encoding="UTF-8")  # создаем файл с исходными данными
data = sequence(random.randint(1, 10))
file1.write(data)  # запись последовательности в файл
file1.close()  # закрытие файла

file2 = open('file_data_2.txt', 'w+', encoding="UTF-8")  # создаем файл с обработанными данными
list_data = list(map(int, data.split(" ")))  # Данные в виде списка
number_crat = [str(x) for x in list_data if x % 3 == 0]  # список чисел, которые кратны 3-м

# Запись обработанных данных в файл 2
file2.writelines([f'Исходные данные: {data}\n',
                  f'Количество элементов: {len(list_data)}\n',
                  f'Минимальный элемент: {min(list_data)}\n',
                  f'Числа кратные трем: {" ".join(number_crat)}\n',
                  f'Количество чисел кратных трем: {len(number_crat)}\n', ])
file2.close()
