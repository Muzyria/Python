def reverse(sequence):
    for i in sequence[::-1]:
        yield i


print(*reverse([1, 2, 3, 4, 5]))

generator = reverse('beegeek')
print(type(generator))
print(*generator)
