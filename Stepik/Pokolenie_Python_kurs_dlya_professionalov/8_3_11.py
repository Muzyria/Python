def get_fast_pow(a: int, n: int):
    if n == 0:
        return 1
    if n % 2 == 0:
        return get_fast_pow(a * a, n / 2)
    else:
        return a * get_fast_pow(a * a, n // 2)


print(get_fast_pow(2, 10))
print(get_fast_pow(5, 2))
print(get_fast_pow(2, 100))
