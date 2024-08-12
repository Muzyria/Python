
def aggregation(func, sequence, initial=None):
    if initial:
        sequence.insert(0, initial)
    ANS = [sequence[0]]
    for i in sequence[1:]:
        ANS.append(func(ANS[-1], i))
    return ANS[1:][-1]


def get_add(x, y):
    return x + y


print(aggregation(get_add, [5, 2, 4, 3, 5], initial=10))
