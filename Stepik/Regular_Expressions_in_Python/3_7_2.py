print(*[i for i in __import__('re').findall(r'https://imgur\.com/[a-zA-Z0-9]{7}', input())], sep='\n')
