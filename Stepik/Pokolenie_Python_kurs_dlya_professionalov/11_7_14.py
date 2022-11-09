import re

word, string = input(), input()
print(len(re.findall(fr'\b({word[0:-3]}(o|ou)r)\b', string, re.I)))