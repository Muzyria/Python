import re

text = re.sub(r'(его|её|их|Его|Её|Их)[а-яё]+', r'\1', input())
print(text)
