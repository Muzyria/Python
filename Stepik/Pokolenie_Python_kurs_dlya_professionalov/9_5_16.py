def power(dergee):
    def fun(x):
        return x ** dergee
    return fun


square = power(2)
print(square(5))

print(power(3)(3))
