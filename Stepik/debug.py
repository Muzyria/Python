from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _from_int(data):
        return f'Целое число: {data}'

    @format.register(f)
    @staticmethod
    def _from_int(data):
        return f'Целое число: {data}'