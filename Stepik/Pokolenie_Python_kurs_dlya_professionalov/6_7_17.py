from collections import Counter


[print(f'{k}: {v}') for k, v in Counter(sorted(input().split(','))).items()]
