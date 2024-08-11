
def aggregation(func, sequence):
    ANS = [sequence[0]]
    for i in sequence[1:]:
        ANS.append(func(ANS[-1], i))
    return ANS[1:]


def get_product(x, y):
    return x * y

print(aggregation(get_product, [2, 6, 5, 10, 5, 1, 2]))
