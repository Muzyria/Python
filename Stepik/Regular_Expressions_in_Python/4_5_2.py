import re

res = re.sub(r'\d+', lambda x: str(int(x[0]) ** 2), input())
print(res)
