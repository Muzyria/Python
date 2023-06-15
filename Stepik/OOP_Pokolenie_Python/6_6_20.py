from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        file_obj = open(filename, mode=mode)
    except Exception as err:
        yield None, err
    else:
        try:
            yield file_obj, None
        finally:
            file_obj.close()
