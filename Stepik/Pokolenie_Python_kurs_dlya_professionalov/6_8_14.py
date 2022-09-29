from collections import Counter


words = Counter(input().lower().split())
n = words.most_common()[0][1]

print(max([i[0] for i in sorted(words.most_common()) if i[1] == n]))
