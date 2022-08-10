
import sys


data = [int(line.strip()) for line in sys.stdin]
if data:
    print(f'Рост самого низкого ученика: {min(data)}')
    print(f'Рост самого высокого ученика: {max(data)}')
    print(f'Средний рост: {sum(data) / len(data)}')
else:
    print('нет учеников')
