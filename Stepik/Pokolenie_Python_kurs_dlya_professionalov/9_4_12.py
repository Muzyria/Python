# new_print = print
#
#
# def print(*args, sep=" ", end=""):
#     a = map(lambda x: x.upper() if isinstance(x, str) else x, args)
#     new_print(*a, sep=sep.upper(), end=end.upper())

my_func = print


def print(*args,  sep=' ', end='\n'):
    lst = map(lambda x: x.upper() if type(x) is str else x, args)
    my_func(*lst, sep=sep.upper(), end=end.upper())

print('beegeek', [1, 2, 3], 4)
