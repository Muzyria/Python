from collections import Counter, ChainMap
y = input()

data = sorted(set(y.split(',')))
counter = Counter(y.split(','))

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

chain_map = ChainMap(bread, meat, sauce, vegetables, toppings)

max_len = len(max(data, key=len))
total = 0
str_len = 0

for elm in data:
    total += chain_map[elm] * counter[elm]
    str1 = f'{elm.ljust(max_len)} x {counter[elm]}'
    str_len = len(str1)
    print(str1)

str2 = f'ИТОГ: {total}р'
if len(str2) > str_len:
    str_len = len(str2)

print('-' * str_len)
print(str2)
