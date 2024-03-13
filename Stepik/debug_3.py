from sys import getsizeof

def cubes_of_odds(iterable):
    return (i**3 for i in iterable if i % 2)

print(*cubes_of_odds([1, 2, 3, 4, 5]))