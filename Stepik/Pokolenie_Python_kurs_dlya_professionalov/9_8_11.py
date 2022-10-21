import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {wrapper.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {wrapper.__name__}(): {repr(func(*args, **kwargs))}')
        return func(*args, **kwargs)
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'
say('Jane', 'Hello, World')
# TRACE: вызов say() с аргументами: ('Jane', 'Hello, World'), {}
# TRACE: возвращаемое значение say(): 'Jane: Hello, World'

@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c
print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)
# sub
# прекрасная функция
# TRACE: вызов sub() с аргументами: (20, 5), {'c': 10}
# TRACE: возвращаемое значение sub(): 25