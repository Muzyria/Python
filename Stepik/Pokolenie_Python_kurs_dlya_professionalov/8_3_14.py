cache = {1: 1, 2: 1, 3: 1}
def tribonacci(n):
    result = cache.get(n)
    if result is None:
        result = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
        cache[n] = result
    return result


print(tribonacci(1))
print(tribonacci(7))
print(tribonacci(4))
