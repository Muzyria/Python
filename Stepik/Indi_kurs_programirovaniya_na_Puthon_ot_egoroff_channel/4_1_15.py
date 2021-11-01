x = map(int, (input().split()))              # Кол-во элементов списков n, m
n = list(map(int, input().split()))        # Список 1
m = list(map(int, input().split()))       # Список 2
f = []
s = n + m
while len(s) > 0:
    f.append(s.pop(s.index(min(s))))
print(*f)    