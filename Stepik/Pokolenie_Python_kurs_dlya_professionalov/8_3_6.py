def func(n):
    if not n:
        return 0
    else:
        return 1 + func(n[1:])


print(func(input()))
