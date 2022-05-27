x = int(input())
print("YES" if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0) else "NO")