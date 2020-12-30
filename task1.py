"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from time import time
import random


def count_time(func):
    def get_time():
        start_time = time()
        func()
        print(time() - start_time)
        return func()

    return get_time


@count_time
def add_list():
    mylist = random.sample(range(0, 1000), 100)
    return mylist


@count_time
def add_dict():
    mydict = {x: random.random() for x in range(1000)}
    return mydict


if __name__ == '__main__':
    my_list = add_list()
    my_dict = add_dict()
    print(my_list)
    print(my_dict)

''' Вывод время заполнения словаря больше потому что словарь это хеш таблица. 
Для ее формирования требуется больше памяти'''
