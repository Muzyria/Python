import re


pattern = r'\d{13,}'
result = re.fullmatch(pattern, input())
if result:
    print(True)
else:
    print(False)