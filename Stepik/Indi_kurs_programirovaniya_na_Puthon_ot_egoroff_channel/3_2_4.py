n=int(input())
if abs(n % 2) == 0:
    print(abs(n // 2))
elif n == 1:
    print(0)
else:
    print(n)
