def decorator(func):
    def wrapper(*args, **kwargs):
        print('---Start calculation---')
        result = func(*args, **kwargs)
        print(f'---Finish calculation. Result is {result}---')
        return result
    return wrapper


@decorator
def add(*values):
    return sum(values)

add(1, 4, 5, 6)
