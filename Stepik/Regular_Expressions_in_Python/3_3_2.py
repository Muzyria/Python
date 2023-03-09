import re

result = re.search(r'#[a-zA-Z]+', input())

print(result.group() if result else "")
