import time
from math import factorial  # функция из модуля math


def get_the_fastest_func(funcs: list, arg):
    result = float('inf')
    result_func = ''
    for func in funcs:
        stat = time.perf_counter()
        n = func(arg)
        end = time.perf_counter()
        func_time = end - stat
        if func_time < result:
            result = func_time
            result_func = func
    return result_func


def factorial_recurrent(n):  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):  # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def for_and_append(iterations):  # с использованием цикла for и метода append()
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension(iterations):  # с использованием списочного выражения
    return [i + 1 for i in range(iterations)]


def for_and_append_2(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension_2(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


if __name__ == '__main__':
    func_list = [factorial, factorial_classic, factorial_recurrent]
    print(get_the_fastest_func(func_list, 900))
    funcs = [for_and_append, list_comprehension]
    print(get_the_fastest_func(funcs, 10_000_000))
    funcs2 = [for_and_append_2, list_comprehension_2, list_function]
    print(get_the_fastest_func(funcs2, range(100_000)))
