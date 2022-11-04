from itertools import groupby


def ranges(numbers):
    result = []
    for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
        group = tuple(group)
        group = group[0], group[-1]
        result.append(group)
    return result


numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))
# [(1, 4), (7, 8), (10, 10)]
