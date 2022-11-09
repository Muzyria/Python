import re

string, word = input(), input()

print(len(re.findall(fr'\b({word})\b', string)))
