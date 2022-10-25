def get_min_max(iterable) -> tuple:
    try:
        min_number = max_number = next(iter(iterable))
        for number in iterable:
            if number < min_number:
                min_number = number
            if number > max_number:
                max_number = number
        return min_number, max_number
    except StopIteration:
        pass


iterable = iter(range(10))
print(get_min_max(iterable))

iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))

iterable = iter([])
print(get_min_max(iterable))

data = iter(range(100_000_000))
print(get_min_max(data))
