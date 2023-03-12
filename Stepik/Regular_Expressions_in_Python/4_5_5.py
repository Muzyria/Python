import re

print(re.sub(r'\b\d+\b',lambda x: str(int(x[0]) // 3) if int(x[0]) % 3 == 0 else x[0], input()))
