import re

print(re.sub(r'[ap]m', lambda x: str(['am', 'pm'][x[0] == 'am']), input()))
