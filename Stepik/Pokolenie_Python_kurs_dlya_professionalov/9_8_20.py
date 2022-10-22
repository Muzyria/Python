import functools


# def strip_range(start: int, end: int, char='.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = list(func(*args, **kwargs))
#             if start > len(value):
#                 return ''.join(value)
#             elif end > len(value):
#                 for i in range(start, len(value)):
#                     value[i] = char
#                 return ''.join(value)
#             else:
#                 for i in range(start, end):
#                     value[i] = char
#                 return ''.join(value)
#         return wrapper
#     return decorator

import functools
def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value[:start] + char * len(value[start:end]) + value[end:]
        return wrapper
    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'
print(beegeek())


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'
print(beegeek())


@strip_range(20, 30)
def beegeek():
    return 'beegeek'
print(beegeek())