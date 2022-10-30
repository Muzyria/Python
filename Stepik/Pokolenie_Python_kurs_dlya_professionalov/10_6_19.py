def interleave(*args):
    return (j for i in zip(*args) for j in i)

# def interleave(*args):
#     for i in zip(*args):
#         yield from i


print(*interleave('bee', '123'))
# b 1 e 2 e 3

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]
print(*interleave(numbers, squares, qubes))
# 1 1 1 2 4 8 3 9 27
