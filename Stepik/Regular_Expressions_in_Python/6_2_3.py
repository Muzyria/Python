import re


def get_x(m):
    return {'o': 'x', 'O': 'X'}[m[0]]


print(re.sub(r'(?i)O', get_x, input()))
