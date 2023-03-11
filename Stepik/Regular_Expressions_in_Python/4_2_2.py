import re

pattern = r"<\/?(\w+).*?>"
tags = re.findall(pattern, input())
print(tags)
