#!/home/max/Загрузки/Python-3.10.2/python
# -*- coding: utf-8 -*-
__version__ = 'v 1.0'
'''
Останавливает и запускает циклическое чтение или запись
в основном приложении при режимах 2 и 3.
Для остановки чтения нужно ввсести в консоль 0, 
для запуска любое дргое число 
'''
from DB_module import change_value_in_db


def run_while():
    while True:
        print("Введите любое значения int для запуска цикла", "\n",
              "для для остановки введите 0")
        if int(input()) != 0:
            change_value_in_db(1)
        else:
            change_value_in_db(0)
            break


if __name__ == '__main__':
    run_while()
