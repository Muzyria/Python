import re

string, word = input(), input()

print(len(re.findall(fr'\B({word})\B', string)))
