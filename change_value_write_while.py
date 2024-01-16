#!/usr/bin/python3
# -*- coding: utf-8 -*-
__version__ = 'v 1.0'
"""
Программа для подстановки значений регистров в БД
для использования режимов с циклической записью
"""
from DB_module import change_values_in_db


def input_values():
    while True:
        print("Введите значения для записи int через пробел", "\n",
              "для выхода введите любую букву \n =>")
        try:
            items = list(map(int, input().split()))
        except ValueError:
            break
        # length_list = len(items)
        count = 0
        for item in items:
            print(" Значение регистра: ", count, " изменено на: ", item)
            change_values_in_db(item, count)
            count += 1


if __name__ == '__main__':
    input_values()
