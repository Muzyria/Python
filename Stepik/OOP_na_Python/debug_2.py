def counting_calls(func: callable) -> callable:
    def inner(*args, **kwargs):
        inner.calls.append({"args": args, "kwargs": kwargs})
        inner.call_count += 1
        return func(*args, **kwargs)
    inner.call_count = 0
    inner.calls = []
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print('Количество вызовов =', add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])
