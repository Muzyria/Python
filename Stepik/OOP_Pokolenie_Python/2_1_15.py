
def intersperse(iterable, delimiter):
    if iterable:
        my_iter = iter(iterable)
        yield next(my_iter)
        for item in my_iter:
            yield delimiter
            yield item


print(*intersperse([1, 2, 3], 0))
print(*intersperse('beegeek', '!'))
print(*intersperse('A', '...'))

iterable = iter('Beegeek')
print(*intersperse(iterable, '+'))