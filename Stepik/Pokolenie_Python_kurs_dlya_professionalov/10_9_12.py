from itertools import dropwhile


# def drop_while_negative(iterable):
#     for i in dropwhile(lambda x: x < 0, iterable):
#         yield i

def drop_while_negative(iterable):
    yield from dropwhile(lambda x: x < 0, iterable)

# drop_while_negative = lambda it: dropwhile(lambda n: n < 0, it)


numbers = [-3, -2, -1, 0, 1, 2, 3]
print(*drop_while_negative(numbers))
# 0 1 2 3

iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])
print(*drop_while_negative(iterator))
# 0 1 2 3 -4 -5 -6

iterator = iter([-3, -2, -1, -4, -5, -6])
print(list(drop_while_negative(iterator)))
# []
