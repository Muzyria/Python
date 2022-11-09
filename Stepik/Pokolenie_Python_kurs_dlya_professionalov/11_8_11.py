import re
from keyword import kwlist


def fun(word):
    if re.findall(fr'\b{word.group()}\b', ' '.join(kwlist), re.I):
        return f'<kw>'
    return word.group()


print(re.sub(f'(\w+)', fun, input()))
