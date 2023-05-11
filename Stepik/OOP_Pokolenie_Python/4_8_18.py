from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _int_format(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def _float_format(data):
        print(f'Вещественное число: {data}')

    @format.register(list)
    @staticmethod
    def _list_format(data):
        print(f'Элементы списка: ', end='')
        print(*data, sep=', ')

    @format.register(tuple)
    @staticmethod
    def _tuple_format(data):
        print(f'Элементы кортежа: ', end='')
        print(*data, sep=', ')

    @format.register(dict)
    @staticmethod
    def _dict_format(data):
        print(f'Пары словаря: ', end='')
        print(*list(data.items()), sep=', ')


Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
