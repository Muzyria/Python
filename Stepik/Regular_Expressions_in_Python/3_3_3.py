import re

result = re.search(r'[Кк]од(.*?)?\: (.?)+', 'Секретный код: Dogecoin')

print(result if result else "")