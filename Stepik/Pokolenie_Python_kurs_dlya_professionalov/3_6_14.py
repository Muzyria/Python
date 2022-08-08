import time


def get_the_fastest_func(func, arg):
    lst = []
    for i in func:
        start = time.perf_counter()
        i(arg)
        end = time.perf_counter()
        lst.append((i, (end - start)))
    print(*lst, "---", sep="\n")
    s = min(lst, key=lambda x: x[1])
    return s[0]


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


funcs = [for_and_append, list_comprehension, list_function]
print(get_the_fastest_func(funcs, range(100_000)))
