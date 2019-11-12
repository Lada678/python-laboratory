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

print('Лабораторна робота номер 1, варіант 9, задача 2')
print('Кондрашової В.О. КМ-93')
print('Знаходження кількості цілих  чисел введених  з клавіатури')
count = 0
a = input('Введите 1 число: ')
a = floatCheck(a)
if int(a) == a:
    count = count + 1
b = input('Введите 2 число: ')
b = floatCheck(b)
if int(b) == b:
    count = count + 1
c = input('Введите 3 число: ')
c = floatCheck(c)
if int(c) == c:
    count = count + 1
print('Кількість цілих чисел серед a,b,c:', count)
