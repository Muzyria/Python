import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n == times:
                        raise MaxRetriesException
        return wrapper
    return decorator


@retry(3)
def no_way():
    raise ValueError
try:
    no_way()
except Exception as e:
    print(type(e))

