def add_attrs(**kwarg) -> callable:
    def decorator(func: callable) -> callable:
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        inner.__dict__.update(kwarg)
        return inner
    return decorator


@add_attrs(test=True, ordered=True)
def add(a, b):
    return a + b

print(add(10, 5))
print(add.test)
print(add.ordered)