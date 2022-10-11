def tribonacci(n):
    if n in range(1, 4):
        return 1
    elif n == 4:
        return 3
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


print(tribonacci(1))
print(tribonacci(7))
print(tribonacci(4))
