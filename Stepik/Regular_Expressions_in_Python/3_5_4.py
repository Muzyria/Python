import re


print(bool(re.fullmatch(r'\+?(\d[( )-]{0,2}){11,}', input())))
