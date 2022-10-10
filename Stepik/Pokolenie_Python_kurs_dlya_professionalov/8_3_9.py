def range_sum(numbers: list, start: int, end: int):
    if start == end:
        return numbers[start]
    else:
        return numbers[start] + range_sum(numbers, start+1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
