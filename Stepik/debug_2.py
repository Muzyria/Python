

from time import perf_counter

start = perf_counter()

hash('b' * 100_000_000)

end = perf_counter()
print(end - start)                      # результат в секундах
