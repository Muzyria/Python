fib = lambda x: 1 if x in (1, 2) else fib(x - 1) + fib(x - 2)

print(fib(10))