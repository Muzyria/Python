import sys

data = [int(line.strip()) for line in sys.stdin]
arif = [i for i in range(data[0], len(data) + 1)]
geom = [int(data[0] * (data[1] / data[0]) ** (i - 1)) for i in range(1, len(data) + 1)]

if data == arif:
    print('Арифметическая прогрессия')
elif data == geom:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
