print(*[i for i in __import__('re').findall(r'<a[^>]+href="([^"]+)"', input())], sep='\n')
