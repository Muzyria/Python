import re

text = input()
text = re.sub(r'([\d\.\:]+)', r'http://\1', text)
print(text)
