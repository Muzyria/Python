
import re


def convert(string):
    if len(re.findall(r"[a-z]", string)) >= len(re.findall(r"[A-Z]", string)):
        return string.lower()       
    else:
        return string.upper()
 



print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
print(convert('dEfAbC'))
print(convert('ABCdef123'))