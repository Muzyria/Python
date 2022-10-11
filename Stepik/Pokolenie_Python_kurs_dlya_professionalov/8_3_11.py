def get_fast_pow(a: int, n: int):
    if n == 0:
        return 1
    else:
        return a * get_fast_pow(a, n - 1)


print(get_fast_pow(2, 10))
print(get_fast_pow(5, 2))
print(get_fast_pow(2, 100))
