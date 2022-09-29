from collections import Counter


words = Counter(len(word) for word in input().lower().split())
[print(f'Слов длины {i[0]}: {i[1]}') for i in sorted(words.most_common(), key=lambda x: x[1])]
