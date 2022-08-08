import time


def get_the_fastest_func(func, arg):
    lst = []
    for i in func:
        start = time.perf_counter()
        i(arg)
        end = time.perf_counter()
        lst.append((i, (end - start)))
    s = min(lst, key=lambda x: x[1])
    return s[0]
