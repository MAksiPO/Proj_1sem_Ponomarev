"""Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
Составить функцию, которая будет находить на сколько квадратов можно разрезать
данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей
площади."""


def check(str):
    num = input(str)
    while type(num) != int:
        try:
            return int(num)
        except ValueError:
            print("Введи число снова!")
        num = input(str)


def crop(a, b):
    i = 1
    while a > b or a < b:
        if a > b:
            a -= b
        else:
            b -= a
        i += 1
    print(f"Прямоугольник можно разбить на {i} квадратов")


def main():
    a, b = check("Введи сторону А: "), check("Введи сторону В: ")
    crop(a, b)


main()
