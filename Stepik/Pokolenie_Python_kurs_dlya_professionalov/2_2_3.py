
n, x, y, a, b = map(int, input().split())
lst = [i for i in range(1, n+1)]

first = [lst[i] for i in range(x-1, y)][::-1]
lst[x-1:y] = first

second = [lst[i] for i in range(a-1, b)][::-1]
lst[a-1:b] = second

print(*lst)
