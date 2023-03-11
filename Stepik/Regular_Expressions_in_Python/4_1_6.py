import re

pattern = r'<p.*?>(.*?)</p>'
result = re.findall(pattern, input())
print(*result, sep='\n')
