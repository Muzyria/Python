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


def for_and_append(iterations):  # с использованием цикла for и метода append()
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension(iterations):  # с использованием списочного выражения
    return [i + 1 for i in range(iterations)]


funcs = [for_and_append, list_comprehension]
print(get_the_fastest_func(funcs, 10_000_000))
