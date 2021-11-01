n = input().lower()
count = 0
for i in n:
    if n.count(i) > count:
        count = n.count(i)
print(count)