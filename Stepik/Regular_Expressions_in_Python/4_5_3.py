import re

print(re.sub(r'(\b[Аа][а-яА-ЯёЁ]*)', lambda x: str(f'удалено({len(x[0])})'), input()))
