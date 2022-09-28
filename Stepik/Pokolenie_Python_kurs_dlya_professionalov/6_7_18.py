from collections import Counter

res = Counter(sorted(input().split(',')))
max_len = len(max(list(res), key=len))


def price(name):
    return sum([ord(i) for i in name.replace(' ', '')])


[print(f'{key.ljust(max_len)}: {price(key)} UC x {value} = {price(key) * value} UC') for key, value in res.items()]
