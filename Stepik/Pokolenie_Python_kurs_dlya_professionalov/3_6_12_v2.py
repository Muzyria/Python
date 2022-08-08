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


from math import factorial                   # функция из модуля math


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


funcs = [factorial, factorial_recurrent, factorial_classic]

print(get_the_fastest_func(funcs, 900))
