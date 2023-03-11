import re

text = input()
text = re.sub(r'\*\*([\w\s]+)\*\*', r'<strong>\1</strong>', text)
text = re.sub(r'\*([\w\s]+)\*', r'<em>\1</em>', text)
print(text)
