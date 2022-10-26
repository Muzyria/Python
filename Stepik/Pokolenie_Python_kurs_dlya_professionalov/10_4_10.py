class Fibonacci:

    def __init__(self):
        Fibonacci.prev = 0
        Fibonacci.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        res = Fibonacci.next
        Fibonacci.next += Fibonacci.prev
        Fibonacci.prev = res
        return res

# import decimal
#
#
# def formulaFibWithDecimal(n):
#     decimal.getcontext().prec = 10000
#     root_5 = decimal.Decimal(5).sqrt()
#     phi = ((1 + root_5) / 2)
#     a = ((phi ** n) - ((-phi) ** -n)) / root_5
#     return round(a)
#
#
# class Fibonacci:
#     def __init__(self):
#         self.n = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.n += 1
#         return formulaFibWithDecimal(self.n)


# fib = lambda x: 1 if x in (1, 2) else fib(x - 1) + fib(x - 2)


fibonacci = Fibonacci()
print(next(fibonacci))

fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

fibonacci = Fibonacci()
for _ in range(50):
    print(next(fibonacci))
