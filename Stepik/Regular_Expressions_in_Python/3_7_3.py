print(*[i for i in __import__('re').findall(r'(?:[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,3}\b)', input())], sep='\n')
