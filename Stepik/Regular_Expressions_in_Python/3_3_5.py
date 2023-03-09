import re


print(re.search(r'(?:t=[\d\.\+]+)', input()).group())
