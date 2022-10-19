def polynom(x):
    x = x ** 2 + 1
    polynom.values.add(x)
    return x

polynom.values = set()


print(polynom(5))
print(polynom.values)


polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))

for _ in range(10):
    polynom(10)

print(polynom.values)
