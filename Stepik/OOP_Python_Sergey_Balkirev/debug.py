attrs = {'id': int, 'name': str, 'weight': (int, float), 'price': (int, float)}

print(set(str(type(5))).issubset(set(str(attrs['id']))))