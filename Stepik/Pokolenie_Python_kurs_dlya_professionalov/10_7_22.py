# def pairwise(iterable):
#     if type(iterable) is list:
#         val = 1
#         for i in range(len(iterable)):
#             try:
#                 yield iterable[i], iterable[val]
#                 val += 1
#             except IndexError:
#                 val = None
#                 yield iterable[i], val
#     else:
#         iterable = list(iterable)
#         nex = None
#         for i in range(len(iterable)):
#             try:
#                 nex = i + 1
#                 yield iterable[i], iterable[nex]
#
#             except IndexError:
#                 nex = None
#                 yield iterable[i], nex
def pairwise(iterable):
    if iterable:
        t = iter(iterable)
        current = next(t)
        for i in t:
            yield current, i
            current = i
        yield current, None


numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))

iterator = iter('stepik')
print(*pairwise(iterator))

data = map(abs, range(-100, 100))
print(*pairwise(data))
# (100, 99) (99, 98)....
