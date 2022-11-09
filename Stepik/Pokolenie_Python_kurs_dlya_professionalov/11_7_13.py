import re

word, string = input(), input()
print(len(re.findall(fr'\b({word[0:-2]}(se|ze))\b', string, re.I)))
