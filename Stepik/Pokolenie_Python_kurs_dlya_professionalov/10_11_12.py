from itertools import groupby

group_iter = groupby(sorted(input().split(), key=len), key=len)

for key, values in group_iter:
    print(f'{key} -> {", ".join(sorted(list(values)))}')

