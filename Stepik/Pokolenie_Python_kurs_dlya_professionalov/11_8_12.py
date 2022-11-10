import re


print(re.sub(r'\b(\w)(\w)', r'\g<2>\g<1>', input()))
