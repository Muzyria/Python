# def is_iterable(obj):
#     return hasattr(obj, '__iter__')

is_iterable = lambda x: hasattr(x, '__iter__')


print(is_iterable(18731))

print(is_iterable('18731'))

objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))
