from time import perf_counter


def search_time_test(collection, numbers):
    start = perf_counter()

    for num in numbers:
        num in collection

    end = perf_counter()
    return end - start


numbers = range(100000)

d = dict(zip(numbers, numbers))
s = set(numbers)
l = list(numbers)

print(search_time_test(d, numbers))
print(search_time_test(s, numbers))
print(search_time_test(l, numbers))