from itertools import product


def password_gen():
    for i in product(range(10), range(10), range(10)):
        yield ''.join(map(str, i))


# def password_gen():
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 yield str(i) + str(j) + str(k)


passwords = password_gen()
print(next(passwords))
print(next(passwords))
print(next(passwords))
