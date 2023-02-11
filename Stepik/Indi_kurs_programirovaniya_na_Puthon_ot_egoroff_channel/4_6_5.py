a, b = int(input()), int(input())

while a <= b and a != 777:
    print(a) if a % 2 != 0 and a % 3 != 0 else None
    a += 1

