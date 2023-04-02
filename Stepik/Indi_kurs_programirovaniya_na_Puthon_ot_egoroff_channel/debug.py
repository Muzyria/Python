def multiply(*args):
    f = lambda x, y: (x*y, args)
    print(f)


print(multiply(1, 2))