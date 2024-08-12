def count_calls() -> callable:
    def inner() -> None:
        inner.total_calls += 1
    inner.total_calls = 0
    return inner






counter = count_calls()
counter()
counter()
print(counter.total_calls)
counter()
print(counter.total_calls)



