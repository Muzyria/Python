import re

if re.match(r'\b([a-z]+ ){11}[a-z]+\b', input()):
    print('возможно, это seed-фраза')
