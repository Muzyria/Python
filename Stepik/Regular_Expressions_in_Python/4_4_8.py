import re

match = re.search(r"(\d+[₽\$])", input())
print(match.expand(r"Цена данного товара \1") if match else '')
