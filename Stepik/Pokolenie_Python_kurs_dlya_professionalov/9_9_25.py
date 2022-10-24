from functools import lru_cache


@lru_cache()
def ways(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return ways(n-1) + ways(n-4) + ways(n-3)
