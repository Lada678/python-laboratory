import math

import re


def floatValid(num):
    """
    check if it float
    :param num: any
    :return: bool
    """
    if bool(re.fullmatch('\s*\d+(\.\d+)?\s*', num)):
        return True
    else:
        return False

def floatCheck(a):
    """
    if a is float return it or force to enter float
    :param a: any
    :return: float
    """
    while True:
        if floatValid(a):
            return float(a)
        else:
            print("Введите число!")
            a = input()
print('Лабораторна робота номер 1, варіант 9, задача 3')
print('Кондрашової В.О. КМ-93')
print('Обчислення функції в залежності від значення введеної змінної')

x = input('Введіть змінну:')
x = floatCheck(x)
if 0<=x<=1:
    print(x**2-x)
else:
    print(x**2-math.sin(math.pi*(x**2)))
