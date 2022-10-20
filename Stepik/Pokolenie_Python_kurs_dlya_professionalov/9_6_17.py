def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {k: v for k, v in enumerate(matrix, 1)}


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrix))
# {1: [5, 6, 7], 2: [8, 3, 2], 3: [4, 9, 8]}

matrix = [[5.1, 6, 7.94]]
print(matrix_to_dict(matrix))
# {1: [5.1, 6, 7.94]}

annotations = matrix_to_dict.__annotations__
print(annotations['return'])
# dict[int, list[int | float]]

print(*matrix_to_dict.__annotations__.values())
# list[list[int | float]] dict[int, list[int | float]]
