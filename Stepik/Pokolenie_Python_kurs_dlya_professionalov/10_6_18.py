# def all_together(*args):
#     return [variable_1 for variable_2 in args for variable_1 in variable_2]
def all_together(*args):
    return (j for i in args for j in i)


objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
print(*all_together(*objects))

objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]
print(*all_together(*objects))
