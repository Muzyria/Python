import time


def calculate_it(func, *args):
    start = time.monotonic()
    result = func(*args)
    end = time.monotonic()
    return result, end - start


def add(a, b, c):
    time.sleep(3)
    return a + b + c


print(calculate_it(add, 1, 2, 3))
