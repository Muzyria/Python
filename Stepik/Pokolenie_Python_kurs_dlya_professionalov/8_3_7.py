def f(n):
    if not n:
        return 0
    else:
        return n % 10 + f(n // 10)


print(f(int(input())))
