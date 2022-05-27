a, b, c = int(input()), int(input()), int(input())
print("YES" if a + b > c and a + c > b and c + b > a else "NO")