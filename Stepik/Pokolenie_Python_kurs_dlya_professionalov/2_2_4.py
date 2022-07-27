
lst = list(map(int, input().split()))
print(*sorted(set(i for i in lst if lst.count(i) > 1)))

