def around(iterable):
    if iterable:
        t = iter(iterable)
        pref = None
        current = next(t)
        for i in t:
            yield pref, current, i
            pref = current
            current = i
        yield pref, current, None


numbers = [1, 2, 3, 4, 5]
print(*around(numbers))
# (None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)

numbers = [1, 2, 3, 4, 5]
print(*around(numbers))
# (None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)
