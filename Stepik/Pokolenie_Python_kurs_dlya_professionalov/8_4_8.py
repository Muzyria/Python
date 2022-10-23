def dict_travel(data, prefix=''):
    for k, v in sorted(data.items()):
        if type(v) in (str, int):
            print(f'{prefix}{k}: {v}')
        else:
            dict_travel(v, f'{prefix}{k}.')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
