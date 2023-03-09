import re

for k, line in enumerate([input() for _ in range(4)], 1):
    result = re.search(r'[Кк]од', line)
    if result:
        print(k, result.start())
        break
else:
    print('код не найден')
