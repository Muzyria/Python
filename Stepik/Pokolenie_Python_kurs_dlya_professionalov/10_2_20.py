def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    result = filter(lambda x: not predicate(x), iterable)
    return result
