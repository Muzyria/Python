from itertools import combinations


def inversions(sequence):
    count = 0
    for i, j in combinations(range(len(sequence)), 2):
        if sequence[i] > sequence[j]:
            count += 1
    return count


sequence = [3, 1, 4, 2]

print(inversions(sequence))
