print(*[i for i in __import__('re').findall(r'(?:\d{2}/\d{2}/\d{4}|\d{4}/\d{2}/\d{2}|\d{2}\.\d{2}\.\d{4}|\d{4}\.\d{2}\.\d{2})', input())], sep='\n')
