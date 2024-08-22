from itertools import combinations


def inversions(value: list[int]) -> int:
    return len(list(filter(lambda x: x[0] > x[1], combinations(value, 2))))


sequence = [3, 1, 4, 2]

print(inversions(sequence))