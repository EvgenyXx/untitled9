'''
Напишите рекурсивную функцию sum(a, b), возвращающую 
сумму двух целых неотрицательных чисел. Из всех арифметических
операций допускаются только +1 и -1. Также нельзя использовать циклы.

Функция не должна ничего выводить, только возвращать значение.
'''

a = 2
b = 2

def f_1(a, b):
    if a == 0:
        return b
    return f_1(a-1, b+1)