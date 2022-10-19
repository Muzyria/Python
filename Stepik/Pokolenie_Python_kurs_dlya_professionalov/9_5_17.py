def generator_square_polynom(a, b, c):
    def func(x):
        return (a * (x ** 2)) + (b * x) + c
    return func


f = generator_square_polynom(1, 2, 1)
print(f(5))

print(generator_square_polynom(9, 52, 64)(8))

f = generator_square_polynom(26, 83, 22)
print(f(55))
