import functools
class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                print(f'{i}-ый запуск функции.')
                func(*args, **kwargs)
                retry(times)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@retry(3)
def no_way():
    raise ValueError
try:
    no_way()
except Exception as e:
    print(type(e))

