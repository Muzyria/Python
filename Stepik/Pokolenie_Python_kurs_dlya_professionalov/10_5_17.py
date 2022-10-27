from math import sqrt

def primes(left, right):
    for n in range(left, right + 1):
        prime = True
        i = 2
        while i <= sqrt(n):
            if n % i == 0:
                prime = False
                break
            i += 1
        if prime:
            yield n


generator = primes(1, 15)
print(*generator)

generator = primes(6, 36)
print(next(generator))
print(next(generator))

generator = primes(37, 37)
try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')
# 37
# Error
