import re

f, i, o = map(lambda x: x[:-1], input().split())
w = r'[а-я]'
print(re.sub(fr'({f}{w}* {i}{w}* {o}{w}*)|({f}{w}* {i[0]}. {o[0]}.)', r'ФИО', input()))
