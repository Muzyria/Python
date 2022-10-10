def f(n):
    if not n:
        return 0
    else:
        return 1 + f(n[1:])


print(f(input()))
