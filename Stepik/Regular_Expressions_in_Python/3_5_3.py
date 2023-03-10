import re

pattern = r'[a-zA-Z0-9@#\$%\^&\*\(\)_\-\+\!\?]{8,}'
result = re.fullmatch(pattern, input())
print(bool(result))
