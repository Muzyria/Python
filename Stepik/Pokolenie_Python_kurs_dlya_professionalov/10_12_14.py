from collections import namedtuple
import itertools as it

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

w = int(input())
result = []
for i in range(1, len(items)+1):
    for item in set(it.combinations(items, i)):
        if sum(m.mass for m in item) <= w:
            result.append((sum(m.price for m in item), [n.name for n in item]))
try:
    print(*sorted(max(result, key=lambda x: x[0])[1]), sep='\n')
except:
    print('Рюкзак собрать не удастся')
