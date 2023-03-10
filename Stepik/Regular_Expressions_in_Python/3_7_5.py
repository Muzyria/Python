print(*[i for i in __import__('re').findall(r'[0-1][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]', input())], sep='\n')
