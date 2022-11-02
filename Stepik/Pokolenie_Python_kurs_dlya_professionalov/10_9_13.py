from itertools import dropwhile


# def drop_this(iterable, obj):
#     yield from dropwhile(lambda x: x == obj, iterable)

drop_this = lambda it, obj: dropwhile(lambda n: n == obj, it)


numbers = [0, 0, 0, 1, 2, 3]
print(*drop_this(numbers, 0))

iterator = iter('bbbbeebee')
print(*drop_this(iterator, 'b'))

iterator = iter('ssssssssssssssssssssssss')
print(list(drop_this(iterator, 's')))
