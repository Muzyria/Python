def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    result = filter(lambda x: not predicate(x), iterable)
    return result


objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))

numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))
