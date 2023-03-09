import re


pattern = r'\w+\s'
result = re.match(pattern, input())
if result:
    print(f'Первое слово в предложении: {result[0]}')
