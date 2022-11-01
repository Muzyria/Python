def with_previous(iterable):
    prev = None
    for i in iterable:
        yield i, prev
        prev = i


numbers = [1, 2, 3, 4, 5]
print(*with_previous(numbers))

iterator = iter('stepik')
print(*with_previous(iterator))
