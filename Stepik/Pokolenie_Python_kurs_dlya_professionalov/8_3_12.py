def recursive_sum(a, b):
    if b == -1:
        return 0
    else:
        return a + recursive_sum(1, b - 1)


print(recursive_sum(10, 22))
print(recursive_sum(99, 0))
print(recursive_sum(0, 0))
