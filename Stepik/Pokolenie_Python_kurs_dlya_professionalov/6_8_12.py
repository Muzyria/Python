from collections import Counter

print(Counter(input().lower().split()).most_common(1)[0][0])
