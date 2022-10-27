def simple_sequence():
    start = 0
    while True:
        start += 1
        for elem in range(start):
            yield start


generator = simple_sequence()
print(next(generator))
print(next(generator))

generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)
