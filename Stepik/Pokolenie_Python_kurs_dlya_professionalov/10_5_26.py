def palindromes(start=1):
    while True:
        if str(start) == str(start)[::-1]:
            yield start
        start += 1


generator = palindromes()
print(next(generator))
print(next(generator))
print(next(generator))

generator = palindromes()
numbers = [next(generator) for _ in range(30)]
print(*numbers)

generator = palindromes()

for _ in range(10_000):
    next(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# 9002009
# 9003009
# 9004009
# 9005009
# 9006009
# 9007009
# 9008009
# 9009009
# 9010109
