def zip_longest(*args, fill=None):
    min_len_ind = args.index(min(args, key=len))
    max_len_ind = args.index(max(args, key=len))
    ex_len = len(args[max_len_ind]) - len(args[min_len_ind])
    if min_len_ind != max_len_ind:
        for i in range(len(args)):
            if len(args[i]) != len(args[max_len_ind]):
                args[i].extend([fill] * ex_len)
    return list()


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))

data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'],
        [False, False, True, True], [1, 5, 9, 9, 104, -24, 13.4, 'f']]
print(zip_longest(*data, fill='skip'))
