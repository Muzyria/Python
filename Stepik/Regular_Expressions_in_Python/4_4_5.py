import re

text = input()
text = re.sub(r'(\d{2})([\.\/])(\d{2})\2(\d{4})', r'\3\2\1\2\4', text)
print(text)
