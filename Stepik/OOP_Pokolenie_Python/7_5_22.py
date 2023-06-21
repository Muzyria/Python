def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def is_iterator(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__next__')
