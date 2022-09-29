from collections import Counter


words = Counter(input().lower().split())
n = words.most_common()[-1][1]

print(*[i[0] for i in sorted(words.most_common()) if i[1] == n], sep=', ')

