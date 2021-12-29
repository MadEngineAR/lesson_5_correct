"""Задача 2.
Замечание "реализовали через defaultdict, как мы и обсуждали на уроке". - Я реализовал через ООП изначально.
А в данном варианте добавил реализацию через defaultdict.
"""
from collections import defaultdict


def sum_mul_num16(num1, num2):
    dict_int_num_16 = defaultdict(list)
    dict_int_num_16[int(num_1, 16)] = list(num1)
    dict_int_num_16[int(num_2, 16)] = list(num2)
    sum_16 = "{:x}".format(int(num1, 16) + int(num2, 16)).upper()
    mul_16 = "{:x}".format(int(num1, 16) * int(num2, 16)).upper()
    return f'Cумма числа {list(num1)} и числа {list(num2)} равна {list(sum_16)} ' \
           f'Произведение числа {list(num1)} и числа {list(num2)} равна {list(mul_16)}'


# ВАРИАНТ 1 ООП
class Number16:
    def __init__(self, num_16):
        self.num_16 = num_16
        self.num_16_list = list(num_16)

    def __add__(self, other):
        # sum_hex = hex(int(self.num_16, 16) + int(other.num_16, 16)) - получется префикс. Решил через format.
        sum_16 = "{:x}".format(int(self.num_16, 16) + int(other.num_16, 16)).upper()
        return f'Cумма числа {self.num_16_list} и числа {other.num_16_list} равна {list(sum_16)}'

    def __mul__(self, other):
        mul_16 = "{:x}".format(int(self.num_16, 16) * int(other.num_16, 16)).upper()
        return f'Произведение числа {self.num_16_list} и числа {other.num_16_list} равна {list(mul_16)}'

    def __str__(self):
        return f''


# print('Введите первое число_16 :')
# num_1 = Number16(input())  # A2
# print('Введите второе  число_16 :')
# num_2 = Number16(input())  # C4F
# print(num_1 + num_2)
# print(num_1 * num_2)
print('Введите первое число_16 :')
num_1 = input()  # A2
print('Введите второе  число_16 :')
num_2 = input()
print(sum_mul_num16(num_1, num_2))
