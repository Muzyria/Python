import re


pat = r'^(Здравствуйте|Доброе утро|Добрый день|Добрый вечер)'

print(True if re.search(pat, input(), flags=re.I) else False)
