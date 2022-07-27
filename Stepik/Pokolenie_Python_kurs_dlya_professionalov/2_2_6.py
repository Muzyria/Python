
n = int(input())
my_set = set(s for s in input().split(', '))
for _ in range(1, n):
    my_set_2 = set(s for s in input().split(', '))
    my_set = my_set & my_set_2

if my_set:
    print(*sorted(my_set))
else:
    print("Сериал снять не удастся")
