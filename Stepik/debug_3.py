import copy


def get_min_max(iterable):
    try:
        copy_iterable = copy.deepcopy(iterable)
        return min(iterable), max(copy_iterable)
    except:
        return None

iterable = iter(range(10))

print(get_min_max(iterable))


iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

iterable = iter([])

print(get_min_max(iterable))