"""
Задача 4.
Замечание - некоторые операции быстрее с ORDEREDDICT
замеры не отражают реального положения дел
операции обычного словаря быстрее.
"""
# Добавил функции заполнения словарей. Из замеров видно что обычные словари
# все таки быстрее. Использование ordereddiсt оправдано при
# использовании спец.возможностей. Например move_to_end.

from timeit import timeit
from collections import OrderedDict


def dict_move_to_end(dct_sample):
    dct_sample.pop('x')
    dct_sample.update(x=1)
    return dct_sample


def ord_dict_move_to_end(dct_sample):
    dct_sample.move_to_end('x', last=True)
    return dct_sample


def dict_del_first_key(dct_sample):
    dct_sample.pop('y')
    dct_sample.update(y=10, last=False)
    return dct_sample


def ord_dict_del_first_key(dct_sample):
    dct_sample.popitem(last=False)
    dct_sample.update(y=10, last=False)
    return dct_sample


def in_dict(dct_sample):
    for i in range(100):
        dct_sample.update(i=i)
    return dct_sample


def in_ord_dict(dct_sample):
    for i in range(100):
        dct_sample.update(i=i)
    return dct_sample


dict_1 = {'x': 1, 'y': 10, 'z': 100}
dict_2 = OrderedDict([('x', 1), ('y', 10), ('z', 100)])
print(f'Время dict_move_to_end - {timeit("dict_move_to_end(dict_1)", globals=globals(),number=1000)}')
print(f'Время ord_dict_move_to_end - {timeit("ord_dict_move_to_end(dict_2)", globals=globals(),number=1000)}')
print(f'Время dict_del_first_key - {timeit("dict_del_first_key(dict_1)", globals=globals(),number=1000)}')
print(f'Время ord_dict_del_first_key - {timeit("ord_dict_del_first_key(dict_2)", globals=globals(),number=1000)}')
print(f'Время in_dict - {timeit("in_dict(dict_1)", globals=globals(),number=1000)}')
print(f'Время in_ord_dict - {timeit("in_ord_dict(dict_2)", globals=globals(),number=1000)}')
